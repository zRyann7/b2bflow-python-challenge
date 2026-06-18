import sys
from repositories.contacts_repository import ContactsRepository
from services.whatsapp_service import WhatsAppService
from utils.logger import logger


def main():
    whatsapp = WhatsAppService()

    contacts = ContactsRepository.get_contacts()

    if not contacts:
        logger.warning("Nenhum contato encontrado.")
        return

    logger.info(f"{len(contacts)} contato(s) encontrado(s).")

    success_count = 0
    error_count = 0

    for contact in contacts:
        try:
            whatsapp.send_message(
                phone=contact["telefone"],
                name=contact["nome"]
            )

            logger.info(
                f"✅ Mensagem enviada para {contact['nome']} "
                f"({contact['telefone']})"
            )
            success_count += 1

        except Exception as error:
            logger.error(
                f"❌ Erro ao enviar para {contact['nome']} "
                f"({contact['telefone']}) - {error}"
            )
            error_count += 1

    logger.info(
        f"Finalizado: {success_count} enviado(s), "
        f"{error_count} erro(s)."
    )


if __name__ == "__main__":
    main()
