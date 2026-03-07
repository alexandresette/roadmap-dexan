#!/usr/bin/env python3
"""
Verifica se todos os arquivos HTML têm o regex correto (sem quebras literais)
"""

import sys

files = [
    'dashboard.html',
    'roadmap-dexan-final.html',
    'mes-1-fundacao.html',
    'mes-2-validacao.html',
    'mes-3-crescimento.html',
    'mes-4-expansao.html',
    'mes-5-multicanal.html',
    'mes-6-escala-total.html',
    'chat-widget-updated.html'
]

print("\n🔍 VERIFICANDO REGEX EM TODOS OS ARQUIVOS\n")
print("=" * 60)

errors = []

for filename in files:
    try:
        with open(filename, 'rb') as f:
            content = f.read()
        
        # Verificar se tem quebra literal (errado)
        if b".replace(/\n/g, '<br>')" in content:
            errors.append(f"❌ ERRO: {filename} - regex com quebra literal!")
            print(f"❌ {filename} - REGEX QUEBRADO")
        else:
            # Verificar se tem a versão correta
            if b".replace(/\\n/g, '<br>')" in content:
                print(f"✅ {filename} - OK")
            else:
                print(f"⚠️  {filename} - regex não encontrado")
    
    except FileNotFoundError:
        print(f"⚠️  {filename} - arquivo não encontrado")

print("=" * 60)

if errors:
    print(f"\n❌ ENCONTRADOS {len(errors)} ERROS!\n")
    for error in errors:
        print(error)
    print("\nExecute: python3 fix-regex-binary.py\n")
    sys.exit(1)
else:
    print("\n✅ Todos os arquivos OK!\n")
    sys.exit(0)
