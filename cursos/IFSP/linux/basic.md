# Comandos Basicos Linux

- ls -> lista ao conteudo do diretorio
- pwd -> mostra o caminho do diretorio atual
- cd <caminho-diretorio> -> muda o diretorio para o caminho especificado
- cd .. -> volta um nivel no caminho de diretorios
- mkdir <nome-diretorio> -> cria um novo diretorio
- rmdir <nome-diretorio> -> remove o diretorio
- man <comando> - mostra o manual(help)
- cal - mostra o calendario do mes atual
- cal <ano> - mostra o calendario com todos os meses do ano
- mkdir <nome\ com\ espaço> -> a bara diz que o espaço faz parte do parametro
- mkdir 'nome com espaço' -> as aspas faz com que o nome com espaço seja apenas um parametro.
- history -  mostra o historico de comandos usados no terminal
- !<numero de indentificação do historico> - executa novamente o comando
- history -c - limpa o historico
- ctrl u - apaga o comando
- sudo <comando> - executa o comando com permissão de admin
- cat <nome-do-arquivo> -  mostra o conteudo do arquivo
- echo <frase/parametros/retorno> - printa na tela a frase
    - echo <frase> > <nome-do-arquivo> - escreve a frase ou o retorno de um comando no arquivo, substituindo o conteudo existente.
    - echo <frase> >> <nome-do-arquivo> - ao utilizar >> é possivel manter o conteudo ja existente e adicionar o novo conteudo
- date - mostra a data atual, incluindo as horas e o fuso
cp <origem> <destino> - copia um arquivo de um lugar para outro
    cp *.txt <destino> - copia todos os arquivos .txt e move para o destino
rm <caminho> - remove arquivos
    rm *.txt - remove todos os arquivos que terminam com .txt
mv <origem> <destino> - move o arquivo da pasta orgem para o destino
    mv a.txt b.txt - renomeia o arquivo a, mantendo o destino mas alterando o nome
free - mostra a quantidade de memoria do sistema. utilize a flag -m ou -g para mostrar e mega ou gigabytes respectivamente
df - mostra a quantidade disponivel em disco . utilize a flag -h para melhor visualização
du -b <nome-do-arquivo> - mostra quantidade/peso em bytes do arquivo
du -sh * - mostra a quantidade/peso em bytes de cada pasta no diretorio atual
uptime - mostra quanto tempo que a maquina esta ligada
top - mostra um monitor de tarefas (gerenciador de tarefas)
ip address show -  mostra inofrmações sobre a placa de rede incluindo o ip
ip route - mostra o roteador em uso
