import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(json.loads(os.environ["FIREBASE_SERVICE_ACCOUNT"]))
firebase_admin.initialize_app(cred)

sha = os.environ["COMMIT_SHA"]
#one
firestore.client().collection("builds").document(sha).set({
    "commit_sha": sha,
    "commit_message": os.environ["COMMIT_MESSAGE"],
    "commit_author": os.environ["COMMIT_AUTHOR"],
    "github_user": os.environ["GITHUB_ACTOR"],
    "branch": os.environ["BRANCH"],
    "repository": os.environ["REPOSITORY"],
    "artifact_name": os.environ["ARTIFACT_NAME"],
    "run_url": os.environ["RUN_URL"],
    "status": "tests_passed",
    "created_at": firestore.SERVER_TIMESTAMP,
})

print(f"Build record {sha} saved to Firestore")