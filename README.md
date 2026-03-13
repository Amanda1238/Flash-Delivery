---
title: "Flash Delivery"
author: "Amanda Fernanda Lopes Martins"
date: "2025-10-31"
output:
  html_document: default
  pdf_document: default
---


>**Flash Delivery** é um jogo de **logística de entregas**, onde o jogador assume o papel de gerente responsável por coordenar pedidos, entregas.



# Sobre o Jogo

O projeto começa com um **menu principal**, onde o jogador pode escolher diversas interações para fazer toda a logistica de entregas.



##  Opções do Menu Principal

- **Criar um Pedido:**  
  O jogador insere o nome do cliente, e o pedido é **gerado automaticamente**.  
  Cada bairro possui um **tempo de entrega fixo**, simulando diferentes distâncias.

- **Buscar Informações do Pedido:**  
  Permite consultar os pedidos armazenados no histórico, exibindo detalhes como cliente, valor, endereço e status da entrega.

- **Salvar o Jogo:**  
  Permite comprimir os dados usando o algoritmo de Huffman, reduzindo o tamanho das informações e possibilitando salvar o estado do jogo.

- **Fazer o mapa:**
  
  Permite ao usuário cadastrar endereços e visualizar o mapa de duas formas: por uma matriz, que exibe os pesos das conexões, ou por uma lista de adjacência.

- **Buscas pelo mapa:**  
  Permite realizar três tipos de busca: por largura, por profundidade e também identificar
  qual é o caminho mais curto até alcançar o destino.

- **Realizar Entrega:**  
  Permite gerenciar entregas utilizando os algoritmos Kruskal, Welsh-Powell e Tarjan, 
  fornecendo informações detalhadas sobre cada pedido, incluindo a quantidade de 
  parcelas ou notas pagas pelo cliente.

- **Sair:**  
  Encerra o jogo e finaliza a execução do programa.



Cada uma dessas opções faz parte da **simulação da logística de entregas**, permitindo ao jogador gerenciar pedidos, otimizar rotas e compreender conceitos de busca e estrutura de dados de forma prática e divertida.

# Tipo de Complexidade

## Sistema de histórico

Todos os pedidos criados são armazenados em uma **lista dinâmica**, chamada `historico`.Essa lista representa o **histórico de pedidos realizados**.
No menu de buscas, o jogador pode realizar diferentes tipos de pesquisa nos pedidos.
A seguir, estão descritas as principais funcionalidades e suas **complexidades de tempo**:



## Menu de Busca

### 1- Buscar todos os pedidos (Busca Sequencial)
Percorre toda a lista de históricos e exibe todas as comandas registradas.A complexidade dessa 
operação é **O(n)**, pois é necessário visitar todos os elementos da lista.



### 2- Buscar todas as comandas por nome (Busca Sequencial)
Essa busca percorre todos os elementos da lista `historico` verificando se o nome do cliente é igual ao nome digitado.
Como a lista **não está ordenada**, é preciso passar por todos os pedidos até encontrar as ocorrências.

🔹 **Complexidade:** `O(n)`  
🔹 **Tipo de busca:** Sequencial



### 3- Buscar todos os pedidos por bairro (Busca Binária)
Nesta funcionalidade foi implementada uma **busca binária**, com uma abordagem mais elaborada:

1. Primeiro, é criada uma **cópia da lista `historico`**, porém **ordenada por bairro**.  
2. A busca encontra a **primeira ocorrência** do bairro desejado.  
3. Após isso, verifica-se para a **esquerda** e para a **direita** da lista ordenada, adicionando todas as ocorrências iguais a uma **lista secundária**.  
4. Quando não há mais bairros iguais, a busca é encerrada e o programa imprime todas as **comandas pertencentes àquele bairro**.

🔹 **Complexidade:** `O(log n + k)`  
- `O(log n)` pela busca binária principal  
- `k` é o número de ocorrências adicionais encontradas à esquerda e à direita  


### 4. Busca de um Cliente Específico (Busca Binária)

Diferentemente da busca pelos bairros, **não é necessário ordenar o vetor de pedidos**.
Isso acontece porque o **ID de cada pedido é único e incremental**, portanto a lista já se encontra **ordenada naturalmente**.

Assim, utilizamos a **Busca Binária**, que possui complexidade **O(log n)**, tornando a busca muito mais eficiente do que a busca sequencial.
Ela reduz o espaço de busca pela metade a cada comparação.

Quando o pedido é encontrado, o sistema:
- Exibe **todas as informações do pedido**;
- Informa **quanto tempo a busca levou**;
- Mostra **quantas comparações foram realizadas** até o resultado final.

### 5. Associação por nome (Rapin Karp)
Para realizar a busca de um cliente pelo nome, foi utilizado o algoritmo **Rabin-Karp**, 
que compara padrões em strings por meio de **hashing**. Ele converte tanto o texto quanto 
o nome procurado para minúsculas, calcula um hash para a palavra buscada e compara esse 
hash com o hash de cada trecho equivalente no texto, atualizando-o de forma eficiente a 
cada passo sem precisar recalcular tudo. Quando os hashes coincidem, é feita uma 
verificação direta para confirmar a correspondência e garantir precisão.

A complexidade média do Rabin-Karp é **O(n + m)**, onde *n* é o tamanho do texto e *m* 
o tamanho da palavra procurada, tornando-o eficiente para buscas repetidas ou em
textos maiores. No pior caso, quando há muitas colisões de hash, ele pode atingir
**O(n * m)**.

### 6.busca por todos os endereços cadastrado (Busca Sequencial)

Para realizar a busca por endereço, é necessário criar um mapa em que os endereços são cadastrados
e armazenados em uma lista. A busca utilizada é sequencial, pois é preciso percorrer 
obrigatoriamente todos os endereços, resultando em uma complexidade de O(n).


## Salvamento do jogo
Para o salvamento do jogo foi utilizada a estrutura de compressão **Huffman**, permitindo reduzir o tamanho dos dados e armazenar o histórico de forma mais eficiente. A seguir, descrevemos cada etapa do processo e suas complexidades.

1. **Gerar a tabela de frequência**  
Essa etapa percorre todo o texto e conta quantas vezes cada caractere aparece.
A complexidade é **O(n)**, pois o algoritmo lê cada caractere apenas uma vez.

2. **Gerar a fila de prioridades**  
A partir da tabela de frequência, cada caractere é inserido em uma `PriorityQueue`.
Como existem **k** caracteres distintos e cada inserção custa **O(log k)**, temos a complexidade **O(k log k)**.

3. **Construção da árvore de Huffman**  
A fila sempre remove os dois menores elementos e insere um novo nó combinado.
Tanto a remoção quanto a inserção custam **O(log k)**.
Como o processo ocorre **k − 1** vezes, a construção completa possui complexidade **O(k log k)**.

4. **Geração da tabela de códigos (dicionário)**  
Para montar os códigos binários, percorremos toda a árvore e adicionamos `'0'` para o ramo esquerdo e `'1'` para o ramo direito até chegar às folhas.
Como a árvore possui aproximadamente **2k − 1** nós, a complexidade é **O(k)**.

5. **Codificação do texto**  
Cada caractere do texto original é substituído por seu código correspondente.
Isso exige percorrer toda a entrada, resultando em complexidade **O(n)**.

6. **Decodificação do texto**  
O processo lê cada bit do texto comprimido e percorre a árvore até encontrar um caractere.
Assim, a decodificação tem complexidade **O(m)**, onde *m* é o tamanho do texto codificado (normalmente proporcional a *n*).

## Montar o mapa do jogo

Nesta parte do jogo, o usuário pode cadastrar endereços e interligá-los, 
atribuindo pesos que representam o tempo, em minutos, entre o ponto de 
partida e o destino. O mapa pode ser visualizado de duas formas: por uma matriz,
que exibe os pesos, ou por uma lista de adjacência. Além disso, é possível excluir
uma rota específica quando necessário.


- **adicionar_local:** O(n)  
- **adicionar_rota (sem mão dupla):** O(n + m)  
- **remover_rota:** O(n + m)  
- **mostrar_matriz:** O(n²)  
- **mostrar_lista:** O(n + E)

## Buscar caminhos pelo mapa

Essa opção apresenta um submenu com três alternativas: realizar a busca em profundidade,
realizar a busca em largura e executar o algoritmo de Dijkstra, que identifica o caminho
mais curto entre o ponto de origem e o destino.

O algoritmo **BFS** possui complexidade de tempo **O(V + A)**, onde *V* é o número de
vértices e *A* é o número de arestas. Sua complexidade de espaço é **O(V)**, correspondente
à quantidade de endereços armazenados. O mesmo ocorre com o algoritmo **DFS**, que também
apresenta tempo **O(V + A)** e espaço **O(V)**.

<!---(arrumar depois)-->
Já o algoritmo **Dijkstra**, na implementação utilizada possui complexidade de tempo
**O(V²)**, pois a cada iteração é necessário verificar todos os vértices não visitados
para encontrar o de menor distância. Sua complexidade de espaço permanece **O(V)**,
devido ao uso dos vetores de distância, visitados e predecessores.

## Realizar pedido

Para a realização do pedido, utilizamos o algoritmo de **Kruskal** para gerar
a **árvore geradora mínima** do percurso, garantindo o caminho de menor custo 
que conecta todas as localidades envolvidas. A complexidade total do algoritmo 
é **O(E log V)**, onde **E** representa o número de arestas do grafo (ou seja, 
todas as possíveis conexões entre os pontos) e **V** é o número de vértices (as 
localidades ou cidades que serão visitadas).

O algoritmo distribui os pedidos entre os motoristas utilizando o método
**Welsh-Powell**, que colore um grafo de conflitos entre pedidos, garantindo
que pedidos adjacentes (que não podem ser entregues pelo mesmo motorista simultaneamente) 
recebam cores diferentes. Cada cor é associada a um motorista, permitindo identificar 
quais pedidos sairão em uma **subdivisão do pedido** com base em critérios de tempo, 
como janelas de entrega. A complexidade do algoritmo é dominada pela coloração: a 
construção do grafo e ordenação dos vértices custa **O(V log V)**, a verificação das
cores dos vizinhos para cada vértice custa **O(V * Δ)** (onde Δ é o grau máximo) e a 
atribuição final dos motoristas custa **O(V)**, resultando em uma complexidade total 
de **O(V²)** no pior caso, ou **O(V + E)** em grafos esparsos, sendo **V** o número de 
pedidos e **E** o número de conflitos entre eles.

Para decidir quais pedidos cada motorista irá levar, utilizamos o algoritmo 
de **Tarjan**, que identifica **componentes fortemente conectados** no grafo
de pedidos. Cada componente representa um grupo de pedidos que estão interligados
por restrições de tempo ou proximidade, permitindo agrupar entregas que devem ser
consideradas juntas na distribuição.  

A complexidade do algoritmo é **O(V + E)**, onde **V** é o número de pedidos e
**E** é o número de relações de conflito ou restrição entre eles. Isso ocorre 
porque o algoritmo realiza uma **busca em profundidade (DFS)** visitando cada 
vértice uma única vez e analisando cada aresta apenas uma vez. Operações adicionais,
como manipulação da pilha ou cálculo dos valores `low` e `ids`, também são realizadas
em tempo linear, garantindo que o algoritmo seja eficiente mesmo para grafos grandes.

No problema do troco, utilizamos **programação dinâmica bottom-up** para determinar 
a quantidade mínima de notas e moedas que o motorista deve receber do cliente. O 
algoritmo constrói uma tabela que armazena, para cada valor até o total do troco,
o número mínimo de cédulas e moedas necessárias, permitindo reconstruir a solução 
ótima de forma eficiente. A complexidade é **O(N × V)**, onde `N` é o número de
denominações disponíveis e `V` é o valor do troco em centavos, garantindo que o 
cálculo seja rápido mesmo para valores relativamente altos.

Por fim, temos funções adicionais relacionadas à **realização das entregas**. 
Essas funções não apenas processam os pedidos utilizando algoritmos como **Kruskal**,
**Welsh-Powell** e **Tarjan**, mas também atualizam os pedidos adicionando `2` à 
quantidade de entregas. Há ainda funções para **finalizar entregas**, que redefinem 
alguns valores dos motoristas, e para **exibir informações sobre cada motorista**, 
incluindo análises detalhadas de desempenho. Nesse contexto, também é registrado 
**quantas notas o cliente devolveu ao motorista**, resolvendo o problema do troco 
e garantindo que a quantidade mínima de cédulas e moedas seja contabilizada.



# Estrutura de Dados

O sistema utiliza uma **lista dinâmica (`list`)** para armazenar todos os pedidos,
funcionando como um **histórico permanente** onde novos pedidos são inseridos sem 
que os anteriores sejam removidos. Essa estrutura mantém simplicidade e fácil 
acesso aos dados, aproveitando diretamente os recursos internos do Python. 


Para otimizar a busca por cliente, foi utilizado o algoritmo **Rabin-Karp**, 
que aplica uma função de **hash** para comparar padrões de texto de maneira eficiente.
Em vez de comparar caractere por caractere diretamente, o algoritmo calcula um hash da 
palavra procurada e o compara com hashes das subsequências do texto, reduzindo 
significativamente o custo de busca na maioria dos casos.

Para comprimir os dados do jogo foi utilizada a estrutura de Huffman, 
aplicada exclusivamente no momento em que o usuário seleciona a opção *Salvar Jogo*. 
Nessa etapa, todas as informações são codificadas e salvas em um arquivo JSON no 
formato comprimido. Ao iniciar o programa novamente, a main realiza a leitura 
desse arquivo e decodifica os dados usando a árvore de Huffman armazenada, 
permitindo reconstruir o estado completo do jogo e continuar exatamente de onde parou.


# Discussão

A busca binária é um dos métodos mais rápidos para localizar elementos em listas ordenadas,
pois reduz o espaço de busca sucessivamente pela metade. Entretanto, quando o objetivo é
encontrar padrões dentro de um texto, o algoritmo mais eficiente é o Rabin–Karp, já que utiliza
hashing para comparar trechos de forma otimizada, mesmo precisando verificar cada elemento da
lista. Assim, enquanto a busca binária é superior em velocidade para dados ordenados, o
Rabin–Karp se destaca na detecção de padrões textuais.

A compressão de dados é aplicada ao nome e ao endereço da classe *Pedidos*, reduzindo a 
quantidade de bits necessária para armazená-los. Isso permite salvar o arquivo de forma 
mais leve, sem comprometer ou alterar as informações originais. Essa estratégia é 
vantajosa, pois otimiza o espaço de armazenamento mantendo a integridade dos dados.



  
