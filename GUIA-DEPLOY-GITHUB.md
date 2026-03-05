# 🚀 GUIA DE DEPLOY AUTOMÁTICO NO GITHUB

## 📋 PRÉ-REQUISITOS

Antes de começar, você precisa:

### ✅ **1. Conta no GitHub**
- Acesse: https://github.com
- Crie uma conta (se ainda não tem)
- É grátis!

### ✅ **2. Git Instalado**
- Windows: https://git-scm.com/download/win
- Mac: `brew install git` ou baixe em https://git-scm.com/download/mac
- Linux: `sudo apt install git` (Ubuntu/Debian)

### ✅ **3. Arquivos do Projeto**
Certifique-se de ter estes arquivos na mesma pasta:
```
✅ index.html
✅ login.html
✅ roadmap-dexan-final.html
✅ mes-1-fundacao.html
✅ README.md
✅ INSTRUCOES-LOGIN.md
✅ deploy-github.sh (script de deploy)
```

---

## 🎯 MÉTODO 1: DEPLOY AUTOMÁTICO (SCRIPT)

### **Para Windows:**

1. **Instalar Git Bash:**
   - Já vem com o Git for Windows
   - Procure "Git Bash" no menu Iniciar

2. **Abrir Git Bash:**
   - Navegue até a pasta do projeto
   - Ou clique com botão direito na pasta → "Git Bash Here"

3. **Executar script:**
   ```bash
   bash deploy-github.sh
   ```

4. **Seguir instruções:**
   - Cole a URL do seu repositório GitHub quando solicitado
   - Aguarde o upload

### **Para Mac/Linux:**

1. **Abrir Terminal:**
   - Mac: Cmd + Espaço → "Terminal"
   - Linux: Ctrl + Alt + T

2. **Navegar até a pasta:**
   ```bash
   cd /caminho/para/pasta/dexan
   ```

3. **Dar permissão ao script:**
   ```bash
   chmod +x deploy-github.sh
   ```

4. **Executar:**
   ```bash
   ./deploy-github.sh
   ```

5. **Seguir instruções:**
   - Cole a URL do repositório quando solicitado

---

## 🎯 MÉTODO 2: GITHUB DESKTOP (MAIS FÁCIL)

### **Passo a Passo:**

1. **Baixar GitHub Desktop:**
   - https://desktop.github.com
   - Instalar e fazer login

2. **Criar novo repositório:**
   - File → New Repository
   - Nome: `dexan-roadmap`
   - Local: escolha a pasta do projeto
   - Create Repository

3. **Commit inicial:**
   - Escreva: "Deploy inicial - Roadmap Dexan"
   - Clique em "Commit to main"

4. **Publicar no GitHub:**
   - Clique em "Publish repository"
   - Desmarque "Keep this code private" (se quiser público)
   - Publish repository

5. **Ativar GitHub Pages:**
   - Acesse: github.com/seu-usuario/dexan-roadmap
   - Settings → Pages
   - Source: main branch
   - Folder: / (root)
   - Save

6. **Aguardar deploy (1-2 minutos)**

7. **Acessar site:**
   - URL: https://seu-usuario.github.io/dexan-roadmap

---

## 🎯 MÉTODO 3: INTERFACE WEB DO GITHUB (SEM INSTALAR NADA)

### **Passo a Passo:**

1. **Criar repositório:**
   - Acesse: github.com
   - Clique em "+" → "New repository"
   - Nome: `dexan-roadmap`
   - Public ou Private (sua escolha)
   - Create repository

2. **Upload dos arquivos:**
   - Clique em "uploading an existing file"
   - Arraste TODOS os arquivos HTML + README.md
   - Commit message: "Deploy inicial"
   - Commit changes

3. **Ativar GitHub Pages:**
   - Settings → Pages
   - Source: main branch
   - Save

4. **Aguardar (1-2 min)**

5. **Acessar:**
   - https://seu-usuario.github.io/dexan-roadmap

---

## 🔄 ATUALIZAÇÕES FUTURAS

### **Via Script (Método 1):**
```bash
# Edite os arquivos HTML
# Depois execute novamente:
bash deploy-github.sh
```

### **Via GitHub Desktop (Método 2):**
```
1. Edite os arquivos
2. GitHub Desktop mostra mudanças
3. Escreva mensagem do commit
4. Commit to main
5. Push origin (botão azul no topo)
```

### **Via Web (Método 3):**
```
1. Acesse github.com/seu-usuario/dexan-roadmap
2. Clique no arquivo que quer editar
3. Clique no ícone de lápis (edit)
4. Faça as mudanças
5. Commit changes (botão verde)
```

---

## 🔐 CONFIGURAR GIT (PRIMEIRA VEZ)

Se for sua primeira vez usando Git:

```bash
# Configure seu nome
git config --global user.name "Seu Nome"

# Configure seu email (mesmo do GitHub)
git config --global user.email "seu@email.com"

# Verifique
git config --list
```

---

## 🆘 RESOLUÇÃO DE PROBLEMAS

### **"Git não é reconhecido"**
- Instale o Git: https://git-scm.com/downloads
- Reinicie o terminal/computador

### **"Permission denied"**
- Configure credenciais do GitHub
- Use GitHub Desktop (mais fácil)

### **"Repository not found"**
- Verifique se a URL está correta
- Exemplo: https://github.com/seu-usuario/dexan-roadmap.git

### **"Site não carrega"**
- Aguarde 2-5 minutos após ativar Pages
- Verifique se ativou corretamente (Settings → Pages)
- URL correta: https://SEU-USUARIO.github.io/NOME-REPO

### **"404 ao clicar nos links"**
- Certifique-se que TODOS os arquivos foram enviados
- Verifique se os nomes estão exatos
- Todos arquivos devem estar na raiz (não em subpastas)

---

## 📱 EXEMPLO COMPLETO

### **Cenário: Xande quer hospedar no GitHub**

```bash
# 1. Criar repositório no GitHub
#    Nome: dexan-roadmap
#    URL gerada: https://github.com/xandesette/dexan-roadmap

# 2. Abrir Git Bash na pasta do projeto

# 3. Executar:
bash deploy-github.sh

# 4. Quando pedir URL, colar:
https://github.com/xandesette/dexan-roadmap.git

# 5. Aguardar upload

# 6. No GitHub, ativar Pages:
#    Settings → Pages → Source: main

# 7. Site fica disponível em:
https://xandesette.github.io/dexan-roadmap

# 8. Compartilhar com Déa:
#    Acesse: https://xandesette.github.io/dexan-roadmap
#    Login: xande ou dea
#    Senha: Elis&Raika
```

---

## 🎯 CHECKLIST FINAL

Antes de fazer deploy:

- [ ] Git instalado
- [ ] Conta GitHub criada
- [ ] Todos arquivos HTML na mesma pasta
- [ ] README.md presente
- [ ] Senhas configuradas (Elis&Raika)
- [ ] Testado localmente (abre no navegador)

Após deploy:

- [ ] Repositório criado no GitHub
- [ ] Arquivos enviados (visíveis no GitHub)
- [ ] GitHub Pages ativado (Settings → Pages)
- [ ] Site acessível (https://usuario.github.io/repo)
- [ ] Login funcionando
- [ ] Compartilhado com Déa

---

## 🌐 ALTERNATIVAS AO GITHUB PAGES

Se preferir outras opções (todas grátis):

### **Netlify (MAIS FÁCIL):**
```
1. Acesse netlify.com
2. Arraste a pasta
3. Site publicado!
4. URL: https://seu-site.netlify.app
```

### **Vercel:**
```
1. Acesse vercel.com
2. Import projeto
3. Deploy automático
4. URL: https://seu-site.vercel.app
```

### **Cloudflare Pages:**
```
1. Acesse pages.cloudflare.com
2. Upload ou conecte GitHub
3. Deploy
4. URL: https://seu-site.pages.dev
```

**Todas funcionam e são grátis!**

---

## 📞 SUPORTE

### **Documentação oficial:**
- GitHub Pages: https://pages.github.com
- Git: https://git-scm.com/doc
- GitHub Desktop: https://docs.github.com/desktop

### **Vídeos úteis:**
- "Como usar GitHub Pages" (YouTube)
- "GitHub Desktop tutorial" (YouTube)

---

## 🎉 CONCLUSÃO

Escolha o método mais confortável para você:

- **Tech-savvy:** Script automático (Método 1)
- **Visual:** GitHub Desktop (Método 2) ⭐ RECOMENDADO
- **Sem instalar:** Interface web (Método 3)

Todos funcionam! 🚀

---

**Última atualização:** 05/03/2026  
**Versão:** 1.0
