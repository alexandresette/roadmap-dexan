#!/usr/bin/env python3
"""
Script para atualizar o Chat Widget DEXAN com:
- Cores DEXAN (azul #1E40AF e laranja #F97316)
- Limpeza de histórico ao fechar
"""

import re

FILES = [
    'roadmap-dexan-final.html',
    'dashboard.html',
    'mes-1-fundacao.html',
    'mes-2-validacao.html',
    'mes-3-crescimento.html',
    'mes-4-expansao.html',
    'mes-5-multicanal.html',
    'mes-6-escala-total.html'
]

# Ler o novo snippet
with open('chat-widget-updated.html', 'r', encoding='utf-8') as f:
    new_chat = f.read()

def update_chat_in_file(filename):
    """Substitui o chat antigo pelo novo"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar o chat antigo
    pattern = r'<!-- 💬 DEXAN CHAT WIDGET - Início -->.*?<!-- 💬 DEXAN CHAT WIDGET - Fim -->'
    
    # Verificar se encontrou o chat
    if not re.search(pattern, content, re.DOTALL):
        print(f"❌ Chat não encontrado em: {filename}")
        return False
    
    # Substituir
    new_content = re.sub(pattern, new_chat, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Chat atualizado em: {filename}")
    return True

def main():
    print("\n🎨 ATUALIZANDO CHAT WIDGET DEXAN\n")
    print("Mudanças:")
    print("  🎨 Cores DEXAN: #1E40AF (azul) e #F97316 (laranja)")
    print("  🧹 Limpa histórico ao fechar o chat")
    print("  ✨ Hover com gradiente azul→laranja\n")
    print("=" * 60)
    
    success_count = 0
    
    for filename in FILES:
        if update_chat_in_file(filename):
            success_count += 1
    
    print("=" * 60)
    print(f"\n✨ {success_count}/{len(FILES)} arquivos atualizados!\n")
    
    if success_count > 0:
        print("📋 PRÓXIMOS PASSOS:")
        print("   1. git add .")
        print("   2. git commit -m 'Update chat: cores DEXAN + limpar histórico'")
        print("   3. git push origin main")
        print("   4. Aguardar deploy Vercel (~1 min)")
        print("\n🎉 Mudanças:")
        print("   - Botão: azul DEXAN (#1E40AF)")
        print("   - Hover: gradiente azul→laranja")
        print("   - Avatar user: laranja (#F97316)")
        print("   - Histórico: limpa ao fechar chat\n")

if __name__ == '__main__':
    main()
