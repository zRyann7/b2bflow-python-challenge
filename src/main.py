from repositories.contacts_repository import (
    ContactsRepository
)

from services.whatsapp_service import (
    WhatsAppService
)

from utils.logger import logger


def main():

    whatsapp = WhatsAppService()

    contacts = (
        ContactsRepository
        .get_contacts()
    )

    if not contacts:

        logger.warning(
            "Nenhum contato encontrado."
        )

        return

    logger.info(
        f"{len(contacts)} contatos encontrados."
    )

    for contact in contacts:

        try:

            whatsapp.send_message(
                phone=contact["telefone"],
                name=contact["nome"]
            )

            logger.info(
                f"Mensagem enviada para "
                f"{contact['nome']}"
            )

        except Exception as error:

            logger.error(
                f"Erro ao enviar para "
                f"{contact['nome']} "
                f"- {error}"
            )


if __name__ == "__main__":
    main()