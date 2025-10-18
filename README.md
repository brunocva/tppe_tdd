# Campeonato Brasileiro Série A 2025 - Simulador

## Descrição
Este projeto é um simulador do Campeonato Brasileiro Série A de 2025, desenvolvido como parte de um trabalho prático. Ele implementa funcionalidades como sorteio de jogos, cálculo de pontuação, classificação e critérios de desempate, seguindo o sistema de pontos corridos.

## Funcionalidades
- Sorteio de jogos para todas as rodadas, garantindo que não existam jogos repetidos.
- Cálculo de pontuação, vitórias, gols marcados, gols sofridos e saldo de gols.
- Aplicação de critérios de desempate (número de vitórias, saldo de gols, etc.).
- Exibição da classificação atualizada a cada rodada.

## Estrutura do Projeto
```
src/
    campeonato.py  # Gerencia o campeonato e a classificação
    partida.py      # Representa as partidas e seus resultados
    time.py         # Representa os times e suas estatísticas

tests/
    test_campeonato.py # Testes para a classe Campeonato
    test_partida.py    # Testes para a classe Partida
    test_time.py       # Testes para a classe Time
```

## Como Executar
1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Clone este repositório e navegue até a pasta do projeto.
3. Para rodar todos os testes:
   ```bash
   pytest
   ```
4. Para rodar um teste específico:
   ```bash
   pytest tests/test_partida.py
   ```

## Requisitos
- Python 3.10+
- pytest

## Membros do Grupo
| Nome                          | Matrícula   |
|-------------------------------|-------------|
| Bruno C. V. de Araújo         | 221034973   |
|                               |             |
|                               |             |
|                               |             |
|                               |             |
