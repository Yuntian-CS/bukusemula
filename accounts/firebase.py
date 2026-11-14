
import firebase_admin

from django.conf import settings
from firebase_admin import credentials, auth, db


# Initialize Firebase Admin SDK
if not firebase_admin._apps:

    credential = credentials.Certificate(
        str(settings.FIREBASE_SERVICE_ACCOUNT_FILE)
    )

    firebase_admin.initialize_app(
        credential,
        {
            "databaseURL": settings.FIREBASE_DATABASE_URL
        }
    )


def get_user_profile(uid):
    """
    Retrieve user information from Firebase.
    """

    return db.reference(f"Users/{uid}").get() or {}


def create_user_profile(uid, email):

    ref = db.reference(f"Users/{uid}")

    profile = ref.get()

    if not profile:

        role = (
            "admin"
            if uid == settings.FIREBASE_BOOTSTRAP_ADMIN_UID
            else "user"
        )

        profile = {
            "uid": uid,
            "email": email,
            "display_name": email.split("@")[0],
            "role": role,
            "active": True,
        }

        ref.set(profile)

    else:

        updates = {"email": email}

        # Bootstrap administrator cannot accidentally lose admin role
        if uid == settings.FIREBASE_BOOTSTRAP_ADMIN_UID:
            updates["role"] = "admin"

        ref.update(updates)

        profile = ref.get()

    return profile


def update_user_role(uid, role):

    allowed_roles = ["admin", "staff", "user"]

    if role not in allowed_roles:
        raise ValueError("Invalid user role")

    db.reference(f"Users/{uid}").update({
        "role": role
    })


def set_user_status(uid, active):

    firebase_user = auth.get_user(uid)

    auth.update_user(
        firebase_user.uid,
        disabled=not active
    )

    db.reference(f"Users/{uid}").update({
        "active": active
    })

