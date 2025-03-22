# HypnoType

**HypnoType** é um expansor de texto leve e personalizável para Windows, desenvolvido em Python.  
Ele permite que você digite atalhos (shortcuts) como `meu_email` e os substitua automaticamente por textos completos, links, mensagens padrão e muito mais.

Ideal para quem deseja ganhar tempo com respostas repetitivas, comandos longos ou templates personalizados.

---

## ✨ Funcionalidades

### ✅ Expansão de Texto por Atalhos (`shortcut`)

- Digite algo como `meu_email` e ele será automaticamente substituído por `meu@email.com`, enquanto digita.
- Se configurado, a aplicação pode pressionar enter após a substituição do texto

### ✅ CRUD de atalhos (pela interface)

- **Adicionar** atalhos
- **Editar** substituições -- Enter no item da lista
- **Renomear** atalhos -- F2 no item da lista
- **Remover** atalhos com `Delete`

### ✅ Reação auditiva

- Ao expandir um texto, o HypnoType pode emitir um som de confirmação.

## Instalando

Com o Python 3.12+ instalado, rode na raiz do projeto `pip install -r requirements.txt`.

Execute com `python src/main.py`.

## ✅ Checklist de Funcionalidades

- [x] Expansão de texto enquanto digita
- [x] Opção de pressionar enter após digitar
- [x] CRUD de atalhos (Adicionar, editar atalho, editar substituto, remover)
- [ ] Ativar / desativar substituições enquanto o aplicativo estiver rodando
- [ ] Substituir após alguma tecla ao invés de assim que o atalho foi digitado
- [ ] Aplicativo rodar silenciosamente minimizado na bandeja do sistema
- [ ] Substituições dinâmicas: data / hora, por exemplo
- [ ] Painel de configurações para personalizar o comportamento do programa

---

Feito com ❤️ por [Josiel Santos](https://github.com/JosielSantos/)
