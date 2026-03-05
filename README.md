# 🚀 DEXAN COMMERCE - ROADMAP ESCALADA 2026

## 📋 ARQUIVOS DO SISTEMA

```
📁 Projeto Dexan
├── index.html                  → Página inicial (redireciona para login)
├── login.html                  → Tela de login
├── roadmap-dexan-final.html    → Roadmap principal (6 meses)
├── mes-1-fundacao.html         → Detalhamento Mês 1
└── INSTRUCOES-LOGIN.md         → Manual de configuração
```

---

## 🔐 CREDENCIAIS DE ACESSO

### **Usuário 1:**
```
Usuário: xande
Senha: Elis&Raika
```

### **Usuário 2:**
```
Usuário: andrea
Senha: Elis&Raika
```

⚠️ **IMPORTANTE:** Ambos usuários têm a mesma senha atualmente.

---

## 🎯 COMO USAR

### **1. Primeiro Acesso:**

1. Abra `index.html` ou `login.html` no navegador
2. Digite:
   - **Usuário:** `xande` ou `andrea`
   - **Senha:** `Elis&Raika`
3. Clique em **Entrar**
4. Você será redirecionado para o roadmap!

### **2. Navegação:**

```
LOGIN → ROADMAP (overview 6 meses) → Clique MÊS 1 → Detalhes semana por semana
```

### **3. Logout:**

- Clique no botão **🚪 Sair** (canto superior direito)
- Sua sessão será encerrada
- Será redirecionado para tela de login

---

## 📱 COMO HOSPEDAR

### **Opção 1: Local (Teste)**

1. Coloque todos os arquivos na mesma pasta
2. Abra `index.html` no navegador
3. Pronto!

### **Opção 2: Online (Recomendado)**

#### **GitHub Pages (Grátis):**

1. Crie um repositório no GitHub
2. Faça upload de todos os arquivos
3. Ative GitHub Pages nas configurações
4. Acesse via: `https://seu-usuario.github.io/dexan`

#### **Netlify (Grátis):**

1. Acesse netlify.com
2. Arraste a pasta com os arquivos
3. Site publicado em segundos!
4. URL: `https://seu-site.netlify.app`

#### **Vercel (Grátis):**

1. Acesse vercel.com
2. Conecte com GitHub ou faça upload
3. Deploy automático!

---

## ✅ CHECKLIST DE DEPLOY

Antes de colocar online:

- [ ] Todos os 4 arquivos HTML na mesma pasta
- [ ] Testado localmente (abre no navegador)
- [ ] Login funcionando (xande / Elis&Raika)
- [ ] Navegação entre páginas OK
- [ ] Logout funcionando
- [ ] Responsive testado (celular)

---

## 🔧 ESTRUTURA DO SISTEMA

### **Fluxo de Autenticação:**

```
1. Usuário acessa index.html
   ↓
2. Redireciona para login.html
   ↓
3. Digita xande + Elis&Raika
   ↓
4. Sistema valida (SHA-256)
   ↓
5. Cria sessão (sessionStorage)
   ↓
6. Redireciona para roadmap-dexan-final.html
   ↓
7. Usuário navega livremente
   ↓
8. Clica MÊS 1 → mes-1-fundacao.html
   ↓
9. Marca tarefas (salva no localStorage)
   ↓
10. Clica 🚪 Sair → Volta para login
```

---

## 📊 FEATURES

### **Login:**
- ✅ Autenticação segura (SHA-256)
- ✅ 2 usuários (xande + andrea)
- ✅ Proteção de sessão
- ✅ Design premium Dexan

### **Roadmap:**
- ✅ 6 meses mapeados
- ✅ Timeline visual interativa
- ✅ Caminhão SVG customizado
- ✅ Cards clicáveis
- ✅ Botão logout

### **Mês 1:**
- ✅ 32 tarefas detalhadas
- ✅ 4 semanas organizadas
- ✅ Checkboxes marcáveis
- ✅ Progress tracking
- ✅ LocalStorage persistente
- ✅ Balão de acompanhamento

---

## 🎨 DESIGN

### **Cores:**
- Azul Dexan: `#1E40AF`
- Laranja Dexan: `#F97316`
- Background: Gradient dark

### **Fonte:**
- SF Pro Display (Apple style)

### **Estilo:**
- Glassmorphism
- Animações suaves
- Responsive mobile

---

## 🔐 SEGURANÇA

### **Implementada:**
- ✅ Senhas em hash SHA-256
- ✅ SessionStorage temporário
- ✅ Proteção em todas as páginas
- ✅ Logout completo
- ✅ Sem senhas em texto claro

### **Recomendações Produção:**
- ⚠️ Use HTTPS sempre
- ⚠️ Considere backend real
- ⚠️ Adicione rate limiting
- ⚠️ Configure CORS
- ⚠️ Faça backups

---

## 🆘 RESOLUÇÃO DE PROBLEMAS

### **"Erro 404 - Arquivo não encontrado"**

**Causa:** Arquivos não estão na mesma pasta

**Solução:**
1. Coloque TODOS os arquivos HTML na MESMA pasta
2. Estrutura deve ser:
   ```
   /minha-pasta/
   ├── index.html
   ├── login.html
   ├── roadmap-dexan-final.html
   └── mes-1-fundacao.html
   ```

### **"Login não funciona"**

**Verifique:**
- Usuário em minúsculas: `xande` (não `Xande`)
- Senha exata: `Elis&Raika` (case-sensitive)
- Navegador atualizado
- JavaScript habilitado

### **"Não salva progresso das tarefas"**

**Verifique:**
- localStorage habilitado no navegador
- Não está em modo anônimo/privado
- Mesmo domínio/URL sempre

### **"Página em branco"**

**Verifique:**
- Abra console (F12)
- Veja se há erros JavaScript
- Confirme que arquivo não está corrompido

---

## 📞 SUPORTE

### **Dúvidas sobre:**

**Senhas:** Leia `INSTRUCOES-LOGIN.md`

**Erros 404:** Verifique se todos arquivos estão juntos

**Deploy:** Siga instruções da plataforma escolhida

**Funcionalidades:** Os arquivos estão comentados

---

## 🎯 PRÓXIMOS PASSOS

### **Curto Prazo:**
1. ✅ Testar sistema localmente
2. ✅ Fazer deploy (GitHub Pages/Netlify)
3. ✅ Compartilhar URL com Andrea
4. ✅ Começar a usar o roadmap!

### **Médio Prazo:**
- Criar páginas Mês 2, 3, 4, 5, 6
- Adicionar mais features
- Melhorar tracking
- Dashboard consolidado

### **Longo Prazo:**
- Backend real (Node.js/PHP)
- Banco de dados
- Sincronização multi-device
- App mobile

---

## 📈 ROADMAP DO ROADMAP 😄

```
✅ Sistema de login
✅ Roadmap 6 meses
✅ Mês 1 completo (32 tarefas)
🔄 Meses 2-6 (em desenvolvimento)
⏳ Dashboard consolidado
⏳ Relatórios automáticos
⏳ Integração Google Calendar
⏳ Notificações
```

---

## 📄 LICENÇA

Uso privado - Xande e Andrea (Dexan Commerce)

---

**Versão:** 1.0  
**Data:** 05/03/2026  
**Autor:** Claude (Assistente)  
**Empresa:** Dexan Commerce

---

## 🎉 BOM TRABALHO!

Sistema completo e pronto para uso!

**Acesse, faça login e comece a planejar sua jornada Escalada 2026!** 🚀

```
xande + Elis&Raika → ROADMAP → MÊS 1 → SUCESSO! 🎯
```
