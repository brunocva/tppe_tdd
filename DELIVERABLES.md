# Entregáveis — TP1 / TP2 (refatorações aplicadas)

Resumo curto

Aplicamos pequenas refatorações no código para deixar responsabilidades mais claras e
facilitar futuras mudanças. Tudo foi testado e a suíte permanece verde.

O que foi alterado

- `src/campeonato.py`
  - Nova classe `ClassificacaoPrinter` para imprimir a tabela (separação de apresentação).
  - Novo objeto `CombGenerator` para gerar combinações de confrontos.
  - `sortear_jogos` continua gerando as rodadas; partes do algoritmo estão separadas em
    métodos auxiliares para melhorar a leitura.

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