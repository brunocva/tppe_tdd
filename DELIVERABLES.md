# Entregáveis — TP1 / TP2 (refatorações aplicadas)

Resumo curto

Aplicamos pequenas refatorações no código para deixar responsabilidades mais claras e
facilitar futuras mudanças. Tudo foi testado e a suíte permanece verde.

O que foi alterado

- `src/campeonato.py`
  - Sorteio agora embaralha a ordem inicial e gera turno + returno.
  - Registro de confrontos para desempate por confronto direto (quando apenas 2 clubes empatam).
  - Critérios completos de desempate: pontos, vitórias, saldo, gols pró, confronto direto, menos vermelhos, menos amarelos e sorteio final.
  - `ClassificacaoPrinter` (Extract Class) e `CombGenerator` (Substituir Método por Objeto-Método) mantidos.
- `src/equipe.py`
  - Estatísticas passam a guardar cartões vermelhos e amarelos (para desempate).
  - Objeto-método `AtualizacaoEstatisticas` mantido.
- `tests/all_tests.py`
  - Agora executa a suíte via `pytest` diretamente.
- Novos testes em `tests/test_campeonato.py` cobrindo confronto direto e desempate por cartões.

Por que fizemos isso

Essas mudanças tornam o código mais modular: cada peça tem uma responsabilidade única,
o que facilita testar, ler e refatorar sem mexer na lógica principal do campeonato.

Testes

Todos os testes foram executados depois das mudanças:

```powershell
pytest -q
# 31 passed
```

Cobertura

Os testes continuam cobrindo as funcionalidades principais do TP1.

Como revisar localmente

```powershell
cd path/to/tppe_tdd
pytest -q
pytest --cov=src --cov-report=html
```

Próximos passos (opções)

- Aplicar refatorações adicionais conforme a indicação da sua turma (me envie a tabela por matrícula).
- Criar um branch `refactor/tp2` com commits separados por operação e abrir PR para revisão.

Se quiser que eu crie o branch e faça o push, diga o nome do branch que prefere (sugestão: `refactor/tp2`).
