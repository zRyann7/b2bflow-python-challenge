from config.supabase_client import supabase


class ContactsRepository:

    @staticmethod
    def get_contacts(limit=3):

        response = (
            supabase
            .table("contatos")
            .select("*")
            .limit(limit)
            .execute()
        )

        return response.data
