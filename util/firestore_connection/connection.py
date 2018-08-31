import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

CRED = credentials.Certificate(
    "/Users/konsti/vm/tuk.mensa-kl-conv-ai/util/firestore_connection/tuk-mensa-kl-conv-ai-firebase-adminsdk-s5fmi-17678edf98.json")


class FirestoreConnector:

    def __init__(self):
        firebase_admin.initialize_app(CRED)
        self.db = firestore.client()

    def create_document(self, path, data):
        """
        Function for creating documents in Firestore
        :param path: The path in Firestore, where the document should be created.
        :param data: A Dict, containing one or more Key-Value Pairs
        :return:
        """
        if self.validate_document_path(path):
            doc_ref = self.db.document(path)
            doc_ref.set(data)

    def get_document(self, path):
        """
        Function for retrieving a document from Firestore.
        :param path: Path to a document in Firestore
        :return: The document as an Dictionary
        """
        if self.validate_document_path(path):
            doc_ref = self.db.document(path)
            doc = doc_ref.get()
            return doc.to_dict()
        else:
            return {}

    def get_collection(self, path):
        """
        Function for retrieving a collection from Firestore.
        :param path: Path to the collection: "Collection" or "Collection/Document/Subcollection"
        :return: Generator of documents
        """
        if self.validate_collection_path(path):
            doc_ref = self.db.collection(path)
            docs = doc_ref.get()
            return docs
        else:
            return {}

    @staticmethod
    def validate_collection_path(path):
        if len(path.split("/")) % 2 != 1:
            print("The path of a collection must have an odd number of elements.")
            return False
        else:
            return True

    @staticmethod
    def validate_document_path(path):
        if len(path.split("/")) % 2 != 0:
            print("The path of a document must have an even number of elements.")
            return False
        else:
            return True


if __name__ == "__main__":
    connector = FirestoreConnector()
    day = connector.get_document("mensa/2018/0827/2")
    print(day)
