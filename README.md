# qaland
## 1 – Tema
  A Inteligência Artificial para geração de Charts para sessões de Testes Exploratórios.
## 2 - Descrição do projeto
  Com o avanço da tecnologia a inteligência artificial tem se provado uma ferramenta poderosa para auxiliar os profissionais nas mais diversas profissões. 
  Queremos usar o poder da Inteligência Artificial combinada com nossos conhecimentos de Testes Exploratórios para automatizar a geração de Charts.
## 3 - Integrantes da equipe
Ana Carolina , Caroline e Simone
## 4 - Professor de suporte
Rodrigo Cursino
## 5 - Definição do problema
O papel do QA é muito amplo e inclui diversas atribuições ao longo de todo o processo de desenvolvimento de software.
Seja auxiliando nos critérios de aceite e na qualidade de escrita das histórias, pareando com desenvolvedores para auxiliar na criação decenários para testes unitários 
ou acompanhando os logs dos sistemas após um deploy.

Além a criação de cenários , execução de testes, gerenciamento de bugs e levantamento de riscos, tudo isso faz parte do dia a dia de um QA.
Para driblar a falta de tempo com tantas atividades e aumentar sua eficiência o QA utiliza as ferramentas ao seu alcance como a automação de testes que permite executar 
testes críticos ou repetitivos de forma automatizada. 

Alguns QAs também utilizam a inteligência artificial para gerar cenários de testes de acordo com as descrições e critérios definidos nas tarefas.
Porém ainda não existe nada nesse sentido para geração dos charts de testes exploratórios e o conhecimento sobre testes exploratórios não é tão difundido e alguns profissionais acreditam que o teste exploratório seja o
adhoc.

Assim a maioria dos QAS não executa os testes exploratórios seja pela falta de conhecimento sobre esse tipo de testes ou seja sobre a falta de tempo para pesquisar , entender a heurística e montar o chart.

## 6 - Possível solução
Acreditamos que uma possível solução para esse problema seja criar uma página web onde o QA insere uma entrada , utilizamos inteligência artificial para processar esses dados e ter como saída diversos charts onde o
profissional pode escolher o que melhor lhe atende. Assim economizaria tempo de pesquisa das heurísticas sendo necessário apenas escolher o chart, talvez fazer pequenos ajustes e executa-lo.

Além disso teria uma segunda página um tipo de biblioteca onde todas as heurísticas estariam reunidas facilitando o tempo de pesquisa.

## 7- Instalação das dependências
pip install -r requirements.txt

## 8- Para rodar o projeto
uvicorn main:app --reload
