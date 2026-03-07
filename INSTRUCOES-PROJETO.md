# INSTRUÇÕES DO PROJETO - DEXAN COMMERCE

## VISÃO GERAL DO PROJETO

**Nome:** DEXAN Commerce  
**Donos:** Xande (Alexandre Sette) e Déa  
**Localização:** Valinhos, São Paulo, Brasil  
**Fase Atual:** Mês 1 - Fundação (abertura da empresa)  
**Modelo de Negócio:** Revenda no Mercado Livre (SEM importação no início)  
**Mentoria:** Escalada PRO - 12 meses  

---

## CREDENCIAIS E ACESSOS

### Site e Repositórios
- **URL Principal:** https://roadmap.dexancommerce.com
- **URL Dashboard:** https://roadmap.dexancommerce.com/dashboard
- **Repositório Roadmap:** https://github.com/alexandresette/roadmap-dexan
- **Repositório Backend Chat:** https://github.com/alexandresette/dexan-chat-backend
- **Vercel Backend:** https://dexan-chat-backend.vercel.app

### Login do Site
- **Usuários:** `xande` ou `dea`
- **Senha:** `dexan2026`

### GitHub
- **Conta:** alexandresette
- **Email:** alexandresettesf@gmail.com

### Firebase
- **Projeto:** dexan-roadmap
- **Database:** Firestore (para sincronização de tarefas)

---

## ESTRUTURA DO ROADMAP - 6 MESES

### **Mês 1: Fundação (Semanas 1-4)**
- **Meta:** Estruturação e primeiras vendas
- **Tarefas:** 32 tarefas
- **IDs das tarefas:** `m1-w1-t1`, `m1-w1-t2`, etc.
- **Objetivo:** CNPJ, infraestrutura, ML setup, primeiras vendas

### **Mês 2: Validação (Semanas 5-8)**
- **Meta:** R$ 5.000 faturamento
- **Tarefas:** 28 tarefas
- **IDs das tarefas:** `m2-w5-t1`, `m2-w5-t2`, etc.
- **Foco:** Otimização, Product Ads ML

### **Mês 3: Crescimento (Semanas 9-12)**
- **Meta:** R$ 10.000 faturamento
- **Tarefas:** 24 tarefas
- **IDs das tarefas:** `m3-w9-t1`, `m3-w9-t2`, etc.
- **Foco:** Google Ads, automação

### **Mês 4: Expansão (Semanas 13-16)**
- **Meta:** Multi-marketplace e loja própria
- **Tarefas:** 24 tarefas
- **IDs das tarefas:** `m4-w13-t1`, `m4-w13-t2`, etc.
- **Foco:** Shopee, loja própria (Nuvemshop/Yampi)

### **Mês 5: Multicanal (Semanas 17-20)**
- **Meta:** R$ 20.000 faturamento, 4 canais
- **Tarefas:** 24 tarefas
- **IDs das tarefas:** `m5-w17-t1`, `m5-w17-t2`, etc.
- **Foco:** Amazon, 4 canais ativos

### **Mês 6: Escala Total (Semanas 21-24)**
- **Meta:** R$ 30.000 faturamento, Container de importação
- **Tarefas:** 23 tarefas
- **IDs das tarefas:** `m6-w21-t1`, `m6-w21-t2`, etc.
- **Foco:** Processos autônomos, container coletivo Escalada

**Total Geral:** 155 tarefas nos 6 meses

---

## ARQUITETURA TÉCNICA

### **Frontend (Roadmap)**
- **Tecnologia:** HTML, CSS, JavaScript puro
- **Framework:** Nenhum (vanilla JS)
- **Hospedagem:** GitHub Pages + Vercel
- **URLs limpas:** Configuradas via `vercel.json`

### **Arquivos Principais**
```
├── index.html (redireciona para login)
├── login.html (autenticação)
├── dashboard.html (roadmap principal)
├── mes-1-fundacao.html (32 tarefas)
├── mes-2-validacao.html (28 tarefas)
├── mes-3-crescimento.html (24 tarefas)
├── mes-4-expansao.html (24 tarefas)
├── mes-5-multicanal.html (24 tarefas)
├── mes-6-escala-total.html (23 tarefas)
├── vercel.json (configuração URLs)
└── chat-widget-updated.html (template do chat)
```

### **Backend (Chat)**
- **Tecnologia:** Node.js serverless (Vercel)
- **API:** Anthropic Claude API
- **Modelo:** claude-sonnet-4-20250514
- **Endpoint:** `/api/chat`

### **Banco de Dados**
- **Firebase Firestore:** Sincronização de tarefas entre usuários
- **localStorage:** Armazenamento local + histórico do chat

---

## CHAT WIDGET - ESPECIFICAÇÕES

### **Funcionalidades**
- ✅ Histórico salvo no localStorage
- ✅ Formatação markdown (negritos, quebras de linha)
- ✅ Botão limpar histórico (🗑️)
- ✅ Responsivo mobile
- ✅ Emoji de robô (🤖) no avatar
- ✅ Cores DEXAN (azul #1E40AF + laranja #F97316)
- ✅ Degradê azul→laranja no botão e header
- ✅ z-index: 9999 (sempre visível)

### **System Prompt do Backend**
O chat conhece:
- Contexto completo do projeto DEXAN
- Roadmap 6 meses com metas
- Fases: Fundação → Validação → Crescimento → Expansão → Multicanal → Escala
- Mentoria Escalada PRO
- Foco em revenda nacional (sem importação inicial)

### **Armazenamento**
- Chave localStorage: `dexan_chat_history`
- Formato: Array de objetos `{role, content}`

---

## SISTEMA DE TAREFAS

### **IDs das Tarefas**
Formato: `mX-wY-tZ`
- `mX` = Mês (m1, m2, m3, m4, m5, m6)
- `wY` = Semana
- `tZ` = Tarefa

**Exemplos:**
- `m1-w1-t1` = Mês 1, Semana 1, Tarefa 1
- `m3-w9-t5` = Mês 3, Semana 9, Tarefa 5

### **Armazenamento**
- **localStorage:** Tarefas individuais (`m1-w1-t1: "true"`)
- **Firestore:** Sincronização em tempo real entre usuários

### **Carregamento Instantâneo**
Script inline que executa ANTES da página renderizar:
- Lê localStorage procurando tarefas com prefixo correto
- Atualiza contadores e barras imediatamente
- Evita "flash" de conteúdo incorreto

---

## CORES E IDENTIDADE VISUAL

### **Paleta de Cores**
```css
--dexan-blue: #1E40AF (azul principal)
--dexan-orange: #F97316 (laranja destaque)
--dexan-blue-light: #3B82F6
--dexan-orange-light: #FB923C
```

### **Gradientes**
- Chat: `linear-gradient(135deg, #1E40AF 0%, #F97316 100%)`
- Botões: Azul → Laranja no hover

---

## REGRAS CRÍTICAS DE DESENVOLVIMENTO

### **⚠️ NUNCA fazer:**
1. **NÃO use scripts Python em modo texto** para editar arquivos HTML
   - Sempre usar modo binário (`'rb'` e `'wb'`)
   - Evita quebrar regex de quebra de linha

2. **NÃO editar manualmente o regex** `.replace(/\n/g, '<br>')`
   - Deve ser `\\n` (dois backslashes)
   - Verificar com `check-regex.py` antes de commit

3. **NÃO criar scripts de atualização automática** sem modo binário
   - Script `update-chat-colors.py` foi DELETADO por quebrar regex

### **✅ SEMPRE fazer:**
1. **Verificar regex antes de commit:**
   ```bash
   python3 check-regex.py
   ```

2. **Usar modo binário para edições:**
   ```python
   with open(file, 'rb') as f:
       content = f.read()
   # fazer substituições em bytes
   with open(file, 'wb') as f:
       f.write(content)
   ```

3. **Testar em TODAS as páginas:**
   - Dashboard
   - Mês 1, 2, 3, 4, 5, 6
   - Mobile e Desktop

---

## WORKFLOW DE DEPLOY

### **Passo a Passo**
```bash
# 1. Verificar regex
python3 check-regex.py

# 2. Adicionar arquivos
git add [arquivos modificados]

# 3. Commit
git commit -m "Descrição clara 🎯"

# 4. Push
git push origin main

# 5. Aguardar
# Vercel faz deploy automático em ~1-2 minutos
```

### **URLs de Teste**
- Dashboard: https://roadmap.dexancommerce.com/dashboard
- Mês 1: https://roadmap.dexancommerce.com/mes-1-fundacao
- Mês 2: https://roadmap.dexancommerce.com/mes-2-validacao
- (etc...)

---

## TROUBLESHOOTING COMUM

### **Chat não abre:**
1. Verificar erro no Console (F12)
2. Procurar por "Invalid regular expression"
3. Se encontrar: rodar correção binária
4. Limpar cache completo (Ctrl+Shift+Delete)

### **Progresso mostra "0" primeiro:**
1. Verificar se script `loadProgressInstant()` existe
2. Confirmar prefixo correto das tarefas (`m1-`, `m2-`, etc.)
3. Verificar se elementos HTML têm IDs corretos

### **Regex quebrado:**
```bash
# Corrigir TODOS os arquivos
python3 -c "
import glob
for f in glob.glob('*.html'):
    with open(f, 'rb') as file:
        content = file.read()
    content = content.replace(b'.replace(/\n/g', b'.replace(/\\\\n/g')
    with open(f, 'wb') as file:
        file.write(content)
"
```

---

## PRÓXIMAS FEATURES (Backlog)

### **Curto Prazo**
- [ ] Limites de gasto Anthropic API ($5/mês)
- [ ] Analytics de uso do chat
- [ ] Export de tarefas para Excel

### **Médio Prazo**
- [ ] Integração com Trello/Notion
- [ ] Notificações de tarefas
- [ ] Modo escuro

### **Longo Prazo**
- [ ] App mobile nativo
- [ ] Integração com ML API
- [ ] Dashboard de vendas real

---

## CONTEXTO ESTRATÉGICO

### **Fase Atual: Pré-Mentoria**
- Aguardando abertura do CNPJ
- Pesquisando produtos no ML
- Preparando primeira call da mentoria

### **Investimento Inicial**
- Estimado: R$ 5.000 - R$ 9.000
- Inclui: estoque inicial, embalagens, etiquetas, software

### **Modelo de Abastecimento**
- **Fase 1-5:** Revenda nacional (atacadistas, indústrias BR)
- **Fase 6:** Container coletivo (importação da China)

### **Diferencial da Mentoria**
- Container coletivo Escalada (compartilhado entre alunos)
- Reduz investimento individual em importação
- Acesso a fornecedores validados

---

## COMANDOS ÚTEIS

### **Desenvolvimento**
```bash
# Verificar status
git status

# Ver últimos commits
git log --oneline -5

# Verificar regex
python3 check-regex.py

# Iniciar servidor local (se necessário)
python3 -m http.server 8000
```

### **Git Config**
```bash
git config user.name "alexandresette"
git config user.email "alexandresettesf@gmail.com"
```

---

## OBSERVAÇÕES FINAIS

### **Prioridades**
1. **Funcionalidade > Estética** - Chat e tarefas devem sempre funcionar
2. **Performance** - Carregamento instantâneo é crítico
3. **Mobile First** - Maioria dos acessos via celular
4. **Simplicidade** - Evitar over-engineering

### **Princípios**
- Código simples e manutenível
- Comentários claros em português
- Commits descritivos com emojis
- Sempre testar antes de push

---

**Última atualização:** Março 2026  
**Versão:** 1.0  
**Mantido por:** Claude AI + alexandresette
