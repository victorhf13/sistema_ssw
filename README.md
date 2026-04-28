🚚 Sistema de Ocorrências Integrado com API e Banco de Dados (SSW)

Recentemente desenvolvi uma solução web para automatizar o envio e o controle de ocorrências logísticas, simulando uma integração com sistemas de transportadoras via API.

O objetivo foi criar um fluxo simples, mas funcional, para centralizar informações de rastreio e eventos de entrega em um único painel.

🔧 O que foi implementado:
📡 Backend (Flask + SQLite)
API em Flask para receber requisições de token e ocorrências
Integração com banco de dados SQLite para persistência dos dados
Estrutura de tabelas para armazenar:
Tokens de autenticação
Ocorrências de entrega
Endpoint de histórico para consulta dos registros enviados
🌐 Frontend (HTML + JavaScript)
Painel web estilo ERP para operação logística
Formulário para:
Geração de token
Envio de ocorrências (CTe, NFe, código e descrição)
Visualização de histórico em tabela dinâmica
Formatação de datas em padrão brasileiro (PT-BR)
Interface responsiva com foco operacional
📊 Funcionalidades principais
Envio de ocorrências via API (simulando integração com transportadoras)
Armazenamento automático no banco de dados
Histórico completo com atualização em tempo real
Validação e tratamento de dados no backend
Estrutura preparada para futura integração com EDI/API oficial
🚀 Objetivo do projeto

A ideia foi construir uma base funcional para:

Testar integrações com sistemas logísticos reais (como SSW)
Simular envio de ocorrências automatizadas
Criar um painel interno para acompanhamento operacional
Evoluir futuramente para integração via EDI/API oficial de transportadoras
📌 Próximos passos
Implementação de login de usuários
Exportação de arquivos EDI
Integração com APIs reais de transportadoras
Sistema de status em tempo real
