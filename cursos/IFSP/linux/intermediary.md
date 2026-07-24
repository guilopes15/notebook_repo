# Comandos Intermediarios Linux

## Gerenciador de pacotes APT
Advanced Packaging Tool(APT) é uma ferramenta que gerencia pacotes em distribuições baseadas em debian, podendo então instalar, remover, atualizar os pacotes e a propria distruição linux.
A palavra reservada sudo serve como uma permissão de administrador.

- sudo apt install <pacote> -> instala o pacote
- sudo apt update -> verifica se existe atualizações para os pacotes instalados
- sudo apt upgrade -> atualiza de fato do os pacotes
- sudo apt remove <pacote> -> remove o pacote
- apt search <pacote> -> faz uma pesquisa via regex do pacote
- sudo apt dist-upgrade -> atualiza a distribuição linux

## Manipulação de arquivos de texto

- touch <nome-do-atquivo> - cria um arquivo vazio
- cat <nome-do-arquivo> - mostra o conteudo do arquivo
- stat <nome-do-arquivo> - mostra os detalhes do arquivos
- head <nome-do-arquivo> - mostra as 10 primeiras linhas do arquivo
- head -n <numero-de-linhas> <nome-do-arquivo> - especifica o numero das primeiras linhas que serao mostradas.
- tail <nome-do-arquivo> -  mostra as 10 ultimas linhas do arquivo
- tail -n <numero-de-linhas> <nome-do-arquivo> - especifica o numero das ultimas linhas que serao mostradas.
- | - O caractere pipe(|) filtra o conteudo, concatenando comandos. Ex: cat a.txt | tail -1 -> mostra a ultima linha do arquivo a.txt.
- grep <palavra> <nome-do-arquivo> - procura e mostra a palavra ou o termo dentro do arquivo especificado.
    - o grep tambem permite procurar arquivos que contenham determinado texto os caracteres. Ex: grep -lir <palavra> . -> procura a palavra especificado no diretorio atual recursivamente(r), mostrando apenas os nomes dos arquivos(l) ignorando letras maiusculas e minusculas(i)
- find <caminho> <nome/pedaço-do-arquivo> -> procura arquivos pelo nome ou parte do nome.
- awk <filtro/comando> <nome-do-arquivo> -> filtra por coluna. Ex: awk '{print $1}' a.txt -> filtra a primeira coluna do arquivo a.txt
- wc <nome-do-arquivo> - filtra o numero de linhas, palavras e caracteres de um ou mais arquivos.
- sort <nome-do-arquivo> -  mostra o conteudo do arquivo de forma ordenada
- sort -r <nome-do-arquivo> - inverte a ordernação
- uniq <nome-do-arquivo> - mostra o conteudo do arquivo, eliminando repetições.
- diff <nome-do-arquivo1> <nome-do-arquivo2> -  mostra a diferença entre os conteudos dos arquivos.

##  Iteração FOR e WHILE

Podemos criar laços de repetiçao no terminal, dentro laço podemos manipular cada arquivo conforme nossa necessidade. Ex:  for i in *.txt; do ls $i; done -> percorre todos os arquivos que termina em .txt e lista cada um deles.

## Rede

- /etc/resolv.conf - pasta que mantem os registros dos servidores dns
- dig <dominio> - mostra informações sobre o dominio
- ping <dominio> - faz testes basicos de conexão com a internet
- host <domino> - mostra o ip e outras informaçoes como servidor de mail
- iwconfig - mostra informaçoes sobre rede wifi
- wget <link de download> - executa o download especificado. Use a flag -c para downloads grandes, onde é possivel continuar o download de onde parou.
- whois <dominio> - mostra mais informações sobre registro de dominios

## Gerenciamento do processos

- lsusb - lista os dispositivos usb
- lspci - lista os dispositivos pci
- sudo lshw - lista as informações do hardware
    - sudo lshw > lshw.txt - salva as informações do hardware em um arquivo txt
- ctrl + c - finaliza o processo que esta em primeiro plano
- O caractere & permite executar um comando em segundo plano, retornando o PID(identicador) do processo
- jobs - lista os processos em background
- kill %<numero-do-processo> - mata o processo especificado que esta em background.
- ps aux - lista os processos em execução, onde podemos visualizar os pid
- kill -9 <PID> -  mata o processo pelo PID
- killall -9 <nome-do-processo> - mata o processo pelo nome
- seq <numero-final> - gera uma sequencia/contagem ate o numero especificado, é possivel passar o inicio da contagem, especificando antes do numero final.
- ctrl + z - para um processo que esta ocupando o terminal, possibilitando novamente o uso, é possivel retoma-lo de onde parou
- bg - retoma o ultimo processo parado em background
- fg - retoma o ultimo processo parado em foreground

### Fila de processos

- ; -> executa o primeiro processo e, ao terminar, executa o proximo. Ex: sleep 10; echo "obrigado"
- & -> executa o primeiro processo em background e já dispara o proximo.Ex: sleep 10 & echo "obrigado"
- && -> executa o primeiro processo e, caso não resulte em falha, executa o proximo. Ex: sleep 10 && excho "obrigado"
- for i in `seq 10`; do echo "Contando ...$i"; sleep 1; done

### User e Groups

groups -> retorna a lista de grupos do user atual faz parte
groups <nome-do-user> -> retorna alista de grupos de um user especifico
users -> retorna os users ativos no sistema
sudo addgroup <nome-do-grupo> -> cria um novo grupo
sudo usermod -a -G <nome-do-group> <nome-do-user> -> Modifica um user, podendo então adicionar um user a um grupo. É necessario fazer login novamente
sudo adduser <nome-do-user> -> cria um novo user
cat /etc/passwd -> mostra os users do sistema o comando em si mostra os ultimos grupos criados
sudo passwd <nome-do-user> -> altera a senha de um user
sudo deluser <nome-do-user> -> remove o user
su <nome-do-user> -> switch user: permite trocar de user
sudo su -> transforma o user atual em root(admin)
cat /etc/passwd -> mostra os users do sistema

### Pemissões de arquivos e pastas

ls -lh /etc | head -> Lista os primeiros arquivos da pasta etc. A flag -lh permite ver mais detalhes
drwx r-x --- -> Define as permissões de arquivos, sendo o primeiro caractere(d) define se é um arquivo ou pasta, os outros 3 (rwx) define as permissões do user. Os proximos caracteres (r-x) definem as permissões de grupo onde o user se encontra. Veja abaixo as demais definições do formato octal:
    - 7: leitura, escrita e execução (rwx)
    - 6: leitura e escrita (rw-)
    - 5: leitura e execução (r-x)
    - 4: leitura (r--)
    - 3: escrita e execução (-wx)
    - 2: escrita (-w-)
    - 1: execução (--x)
    - 0: nenhuma permissão (---)

chmod 700 <nome-arquivo-ou-pasta> -> Altera a permissão de um arquivo ou pasta. O numero 7 define permissão de leitura, escrita e execução ao user atual, o 0 indica que o grupo que o user faz parte não tem permissão alguma e o outro 0 indica que os demais tambem não possui definição alguma.
    - chmod 755 <nome-arquivo-ou-pasta> -> O numero 5 indica que tanto o grupo quanto os demais user terao permissão de leitura e execução.
    - chmod 750 <nome-arquivo-ou-pasta> -> O numero 0 indica que os demais users n possuiram nenhuma permissão
sudo chown <user:grupo> <nome-pasta-ou-arquivo> -> Change owner: Altera o dono do arquivo ou pasta, podendo então alterar o user e grupo respectivamente.

### Compactadores

- tar -> Permite criar pacotes e comprimi-los. Parametros opcionais:
    - c create
    - z zip
    - v verbose
    - f file
    - x extract
tar czvf files.tar.gz *.txt -> compacta todos os arquivo .txt criando um novo arquivo compactado chamado files.tar.gz. É necessario o extensão .gz ao utilizar o parametro z.
tar xzvf <caminho-do-arquivo-compactado> -> Extrai um arquivo compactado no diretoria atual.

zip f.zip *.txt -> compacta todos os arquivos .txt em um unico arquivo f.zip
unzip <caminho-do-arquiv-compactado> -> descompacta o arquivo zip no diretorio atual

bzip2 *.txt -> compacta todos os arquivos .txt, gerando um novo arquivo .bz2 para cada arquivo especificado
bzip2 -d * -> descompacta todos os arquivos .bz2

gzip <nome-do-arquivo> -> compacta o arquivo especificado em formato .gz
gzip -d <nome-do-arquivo-compactado> -> descompacta o arquivo .gz
