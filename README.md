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
    all_tests.py       # Suíte para executar todos os testes
    test_campeonato.py # Testes para a classe Campeonato
    test_partida.py    # Testes para a classe Partida
    test_time.py       # Testes para a classe Time
```

## Como Executar
1. Certifique-se de ter o Python instalado (versão 3.10 ou superior).
2. Clone este repositório e navegue até a pasta do projeto.
3. Para rodar todos os testes:
   ```bash
   python -m unittest discover -s tests
   ```
4. Para rodar um teste específico:
   ```bash
   python -m unittest tests.test_partida
   ```

## Requisitos
- Python 3.10+

## Melhorias Futuras
- Persistência de dados (salvar e carregar estado do campeonato).
- Interface gráfica para gerenciar o campeonato.
- Automação de testes com CI/CD.
