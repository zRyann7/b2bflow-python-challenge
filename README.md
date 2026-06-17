# B2BFlow Challenge - Integração Supabase + Z-API

Este projeto realiza a leitura de contatos cadastrados em um banco de dados Supabase e realiza o disparo automático de mensagens personalizadas via Z-API utilizando Python.

## 🛠️ 1. Setup da Tabela (Supabase)

Crie uma tabela chamada `contatos` no seu painel do Supabase com a seguinte estrutura SQL:

```sql
create table contatos (
  id bigint generated always as identity primary key,
  nome text not null,
  telefone text not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Inserção de dados de teste (Até 3 registros conforme a regra)
insert into contatos (nome, telefone) values 
('👉 Nome do Avaliador 1', '5511999999999'),
('👉 Nome do Avaliador 2', '5511988888888'),
('👉 Nome do Avaliador 3', '5511977777777');
```

> **Nota:** Certifique-se de que os números de telefone incluam o código do país e o DDD (ex: `55119...`) para garantir o envio correto pela Z-API.

## 🔑 2. Variáveis de Ambiente (`.env`)

Crie um arquivo na raiz do projeto chamado `.env` e preencha com as suas credenciais gratuitas:

```env
# Configurações do Supabase
SUPABASE_URL=https://supabase.co
SUPABASE_KEY=sua-api-key-anon-do-supabase

# Configurações da Z-API
Z_API_INSTANCE_ID=sua-instancia-z-api
Z_API_TOKEN=seu-token-z-api
Z_API_CLIENT_TOKEN=seu-client-token-z-api
```

## 🚀 3. Como Rodar o Projeto

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o script principal:**
   ```bash
   python main.py
   ```
