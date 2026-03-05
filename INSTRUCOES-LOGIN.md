# 🔐 INSTRUÇÕES DE CONFIGURAÇÃO DE LOGIN

## 📋 Como Trocar Usuários e Senhas

### **Arquivo:** `login.html`

---

## 🔑 SENHAS ATUAIS (TEMPORÁRIAS):

```
Usuário: xande
Senha: test

Usuário: andrea  
Senha: test
```

⚠️ **IMPORTANTE:** Troque essas senhas imediatamente!

---

## 🛠️ COMO TROCAR AS SENHAS:

### **Passo 1: Gerar Hash SHA-256 da Nova Senha**

Acesse: https://emn178.github.io/online-tools/sha256.html

1. Digite sua senha desejada
2. Clique em "Hash"
3. Copie o código gerado (64 caracteres)

**Exemplo:**
```
Senha: minhasenha123
Hash: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

---

### **Passo 2: Editar o Arquivo login.html**

Abra `login.html` e localize esta seção (linha ~121):

```javascript
const USERS = {
    'xande': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
    'andrea': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
};
```

**Substitua** os hashes pelos novos:

```javascript
const USERS = {
    'xande': 'SEU_HASH_AQUI',
    'andrea': 'SEU_HASH_AQUI'
};
```

---

### **Passo 3: Adicionar Mais Usuários (Opcional)**

```javascript
const USERS = {
    'xande': 'hash_senha_xande',
    'andrea': 'hash_senha_andrea',
    'outro_usuario': 'hash_senha_outro'
};
```

---

## 🎯 EXEMPLO COMPLETO:

### **Antes:**
```javascript
const USERS = {
    'xande': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',  // test
    'andrea': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'   // test
};
```

### **Depois (exemplo com senhas fortes):**
```javascript
const USERS = {
    'xande': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',   // 123
    'andrea': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'  // 456
};
```

---

## 🔒 SEGURANÇA:

### **Recomendações:**

✅ Use senhas fortes (mínimo 8 caracteres)
✅ Combine letras, números e símbolos
✅ Não compartilhe suas senhas
✅ Troque as senhas periodicamente
✅ Nunca use senhas simples como "123", "senha", etc.

### **Exemplos de Senhas Fortes:**

- `Dex@n2026!`
- `Escal@da#2026`
- `Xand3$Str0ng!`

---

## 🚀 COMO FUNCIONA:

1. **Usuário digita:** usuário + senha
2. **Sistema converte:** senha → hash SHA-256
3. **Sistema compara:** hash digitado = hash armazenado?
4. **Resultado:** ✅ Login ou ❌ Erro

---

## 🆘 PROBLEMAS COMUNS:

### **"Não consigo fazer login"**
- Verifique se digitou usuário corretamente (minúsculas)
- Verifique se a senha está correta
- Confirme se o hash no código está correto

### **"Esqueci minha senha"**
- Gere um novo hash
- Substitua no arquivo login.html
- Salve e recarregue a página

---

## 📱 SESSÃO:

- Login válido por **sessão do navegador**
- Ao fechar o navegador, precisa logar novamente
- Botão "🚪 Sair" encerra sessão imediatamente

---

## 🔐 SEGURANÇA ADICIONAL (FUTURO):

Para mais segurança, considere:
- Hospedar em servidor com HTTPS
- Adicionar autenticação de 2 fatores
- Usar backend real (não só frontend)
- Implementar rate limiting
- Logs de acesso

---

**Última atualização:** 05/03/2026
**Versão:** 1.0
