# PROJETO DEXAN COMMERCE - INSTRUÇÕES CLAUDE PROJECTS

## CONTEXTO DO PROJETO

Você está trabalhando no projeto **DEXAN Commerce**, um roadmap interativo de 6 meses para crescimento de revenda no Mercado Livre.

**Donos:** Xande e Déa (Valinhos/SP)
**Fase:** Mês 1 - Fundação (abertura CNPJ)
**Meta 6 meses:** R$ 0 → R$ 30.000/mês
**Mentoria:** Escalada PRO

---

## ARQUITETURA TÉCNICA

**Frontend:** HTML/CSS/JavaScript vanilla
**Backend Chat:** Node.js serverless (Vercel) + Claude API
**Database:** Firebase Firestore + localStorage
**Deploy:** GitHub → Vercel (automático)

**Repositórios:**
- Roadmap: https://github.com/alexandresette/roadmap-dexan
- Backend: https://github.com/alexandresette/dexan-chat-backend

**Site:** https://roadmap.dexancommerce.com

---

## ESTRUTURA - 6 MESES (155 TAREFAS)

| Mês | Fase | Meta | Tarefas | IDs |
|-----|------|------|---------|-----|
| 1 | Fundação | Estruturação | 32 | m1-wX-tY |
| 2 | Validação | R$ 5k | 28 | m2-wX-tY |
| 3 | Crescimento | R$ 10k | 24 | m3-wX-tY |
| 4 | Expansão | Multi-marketplace | 24 | m4-wX-tY |
| 5 | Multicanal | R$ 20k, 4 canais | 24 | m5-wX-tY |
| 6 | Escala | R$ 30k, Container | 23 | m6-wX-tY |

---

## ARQUIVOS PRINCIPAIS

```
├── dashboard.html (roadmap principal)
├── mes-1-fundacao.html → mes-6-escala-total.html
├── login.html
├── chat-widget-updated.html (template do chat)
├── vercel.json (URLs limpas)
├── check-regex.py (verificador)
└── INSTRUCOES-PROJETO.md (doc completo)
```

---

## CORES DEXAN

```css
Azul: #1E40AF (principal)
Laranja: #F97316 (destaque)
Gradiente: linear-gradient(135deg, #1E40AF 0%, #F97316 100%)
```

---

## ⚠️ REGRAS CRÍTICAS

### NUNCA:
1. ❌ Editar HTML com Python modo texto (`'r'/'w'`)
2. ❌ Criar scripts de atualização automática sem modo binário
3. ❌ Tocar no regex `.replace(/\n/g, '<br>')` manualmente

### SEMPRE:
1. ✅ Usar modo binário (`'rb'/'wb'`) para editar HTML
2. ✅ Rodar `python3 check-regex.py` antes de commit
3. ✅ Testar em TODAS as páginas (dashboard + 6 meses)
4. ✅ Limpar cache ao testar (Ctrl+Shift+Delete)

---

## REGEX CRÍTICO

**Correto:** `.replace(/\\n/g, '<br>')` (dois backslashes)
**Errado:** `.replace(/\n/g, '<br>')` (quebra literal - QUEBRA O CHAT!)

**Verificar:**
```bash
python3 check-regex.py
```

**Corrigir:**
```python
with open(file, 'rb') as f:
    content = f.read()
content = content.replace(b".replace(/\n/g", b".replace(/\\\\n/g")
with open(file, 'wb') as f:
    f.write(content)
```

---

## CHAT WIDGET

**Features:**
- Histórico persistente (localStorage: `dexan_chat_history`)
- Formatação markdown (**negrito**, quebras de linha)
- Botão limpar (🗑️)
- Avatar: 🤖 (assistente), VC (usuário laranja)
- z-index: 9999
- Responsivo mobile

**Backend:**
- URL: https://dexan-chat-backend.vercel.app/api/chat
- Modelo: claude-sonnet-4-20250514
- Max tokens: 1024

---

## SISTEMA DE TAREFAS

**Formato ID:** `mX-wY-tZ`
- m1 = Mês 1, w1 = Semana 1, t1 = Tarefa 1

**Exemplo:** `m1-w1-t1`, `m3-w9-t5`

**Armazenamento:**
- localStorage: tarefas individuais (`m1-w1-t1: "true"`)
- Firestore: sincronização em tempo real

**Carregamento Instantâneo:**
Script inline que lê localStorage ANTES da renderização para evitar "flash" de 0 tarefas.

---

## WORKFLOW DE DEPLOY

```bash
# 1. Verificar regex
python3 check-regex.py

# 2. Git
git add [arquivos]
git commit -m "Descrição 🎯"
git push origin main

# 3. Aguardar Vercel (~1-2 min)
```

---

## TROUBLESHOOTING

**Chat não abre:**
1. Console (F12) → "Invalid regular expression"
2. Rodar `check-regex.py`
3. Corrigir com modo binário
4. Limpar cache

**Progresso mostra 0:**
1. Verificar IDs (`m1-`, `m2-`, etc.)
2. Confirmar `loadProgressInstant()` existe
3. Verificar elementos HTML (IDs corretos)

---

## CONTEXTO ESTRATÉGICO

**Modelo de Negócio:**
- Fase 1-5: Revenda nacional (atacado BR)
- Fase 6: Container coletivo (importação China)

**Investimento:** R$ 5k-9k inicial
**Diferencial:** Container compartilhado Escalada (reduz custo)

---

## PADRÕES DE CÓDIGO

**Git Config:**
```bash
git config user.name "alexandresette"
git config user.email "alexandresettesf@gmail.com"
```

**Commits:** Descritivos com emojis
**Comentários:** Português, claros
**Princípio:** Simplicidade > Over-engineering

---

## PRÓXIMAS FEATURES (BACKLOG)

- [ ] Limites API ($5/mês)
- [ ] Analytics de uso
- [ ] Export Excel
- [ ] Dark mode
- [ ] PWA mobile

---

## COMANDOS ÚTEIS

```bash
# Verificar status
git status

# Últimos commits
git log --oneline -5

# Verificar regex
python3 check-regex.py

# Servidor local
python3 -m http.server 8000
```

---

## OBSERVAÇÕES IMPORTANTES

1. **Performance é crítica** - Carregamento instantâneo obrigatório
2. **Mobile first** - Maioria dos acessos via celular
3. **Sempre testar antes de push**
4. **Documentar mudanças importantes**
5. **Manter código simples e manutenível**

---

**Versão:** 1.0
**Última atualização:** Março 2026
**Mantido por:** Claude AI + alexandresette
