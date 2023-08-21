import os

class Config(object):
    DATABASE = os.environ.get("mongodb+srv://bot_vambir:Al2552001@cluster0.heabj.mongodb.net/vambir_bot?retryWrites=true&w=majority")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6025090138").split())
    SUPPORT = os.environ.get("BXB_KING")
