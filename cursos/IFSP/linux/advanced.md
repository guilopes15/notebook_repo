# Comnados Avançados Linux

## Instalação e configuração do archlinux

- loadkeys br-abnt2 -> configura o teclado para portugues
- cfdisk - abre o utilitario de particionamento de disco
- mkfs.ext4 /dev/sda1 -> formata a partição sda1 com o sistema de arquivos ext4 do linux
    - sda1 -> sata disk A, 1ª partição
    - ext4 -> sistema de arquivos de alta confiabilidade, escalabilidade e desempenho, suportando volumes de até 1 1 EiB(exabyte) e arquivos de até 16 TiB(terabyte).
- mount /dev/sda1 /mnt -> monata a partição sda1 na pasta /mnt
- pacstrap /mnt base linux nano -> instala o archlinux na maquina
- arch-chroot /mnt -> os comandos vão acontecer diretamente na partição da instalação sem a necessidade de dizer em qual partição os arquivos devem se instalados.
- nano /etc/locale.gen -> abre o arquivo de localização(remova o # da lingua de sua preferencia)
- locale-gen -> instala a lingua configurada no comando acima
- echo LANG=pt_BR.UTF-8 > /etc/locale.conf -> escreve a lingua desejado no arquivo de configuração.
- echo KEYMAP="br-abnt2.map.gz" > /etc/vconsole.conf -> escreve no arquivo de configuração o idioma do teclado.
- passwd -> define uma senha de usuario root
- pacman -S grub -> instala o pacote grub. O grub permite selecionar qual sistema operacional sera inicializado.
- grub-install /dev/sda -> instala o grub no registro de inicialização MBR do HD sda:
- mkinitcpio -p linux -> cria o ambiente de inicialização do linux na partição atual.
- grub-mkconfig -o /boot/grub/grub,cfg -> cria a config do grub  e fornece a lista de todos os sistemas operacionais na inicializaçao.
- pacman -S dhcpcd - instala o serciço DHCP(configura os dispositivos em uma rede IP).
- systemctl enable dhcpcd.service -> habilita o dhcp, ficando ativo na inicialização.
- exit; reboot
- ping -c3 8.8.8.8 -> teste a conexão com a internet 3 vezes
- pacman -Syy -> atualiza a lista de pacotes
- pacman -S xf86-video-vesa alsa-utils xorgserver xorg-xinit xorg-twm xorg-xclock xterm xfce4 xfce4-goodies -> instala pacotes necessarios para uma interface gráfica.
- pacman -S ntfs-3g unrar p7zip gparted chromium firefox icedtea-web jre8-openjdk vlc mlocate -> instala pacotes uteis para o uso do dia a dia
- pacman -S ttf-droid ttf-inconsolata -> instala pacotes de fontes
- pacman -S gdm && systemctl enable gdm -> instala pacotes necessarios para o login manager

## Possiveis problemas de VM

- pacman -S linux-headers
- pacman -S virtualbox-guest-utils

## Configurações de usuario

- useradd aluno -> cria o usuario aluno
- mkdir /home/aluno -> cria o caminho e a pasta para o user aluno no sistema
- passwd aluno -> cria uma senha para o user aluno
- chown aluno:aluno /home/aluno -> permite o acesso e a utilização do user aluno ao caminho criado acima.
- pacman -S sudo vi -> instala o sudo e o vi, possibitando a outros users executar tarefas administrativas e editar textos com vi.
- groupadd sudo -> cria o grupo sudo
- usermod -G sudo aluno -> adiciona o user aluno ao grupo sudo
- visudo -> abre o editor de texto para configurar o sudo (desmarque o comando sudo ALL)
- sudo pacman -S network-manager-applet -> instala um network manager, permitindo conectar e desconectar de redes sem usar o terminal
- sudo pacman -S gnome-keyring - instala um confre de senhas, evitando digitar suas senhas a todo momento.
- sudo systemctl enable NetworkManager.service -> habilita o network manager na inicialização

## Outros

- sudo pacman -S cinnamon gnome-terminal mate-themes mate-icon-theme archlinuxwallpaper -> instala outra interface grafica, themes e wallpapers.
- sudo pacman -S libreoffice-still-pt-br -> instala o libreoffice em portugues.


# Instalando e configurando CentOS

- free -m -> verifica memoria ram
- yum update -> verifica e instala os pacotes
yum grouplist - mostra a lista de grupos de pacotes
- yum groupinstall - instala um grupo de pacotes. Ex: yum groupinstall "GNOME Desktop" - instala a inteface grafica Gnome
- systemctl set-default graphical - habilita a interface grafica(GUI)
- yum search libreoffice -> pesquisa pacotes do libreoffice
- yum install <nome-pacote> - instala os pacotes
- yum remove libreoffice -> remove o pacote especificado
- wget <link-de-download> -> baixa pacote via link
- tar xvf <nome-do-pacote-baixado> - descompacta o pacote
- rmp -i <caminho-do-pacote-descompactado> - instala o pacote via arquivo

## Acessando servidor via ssh
 É necessario ter o OpenSSH no servidor que deseja conectar. Caso usar virtual box mudar configuração de rede para modo bridge.

- ssh <ip do servidor> - se conecta a maquina do ip especificado.(é necessario a senha do user). Com a flag -p <porta> é possivel diz exatamente a porta de acesso.
- sudo nano /etc/ssh/sshd_config - abre o arquivo de configuração do ssh, onde é possivel definir a porta de acesso, liberar ou negar acesso a usuarios queiram se conectar a maquina
- sudo /etc/init.d/ssh restart - reinicia o ssh para ativar a configuração alterada
- sudo adduser <nome> - cria um novo user
- ssh <nome-do-user>@<ip-do-servidor> -p <porta> - acessa a maquina via ssh usando o usuario especificado

O no arquivo de configuração sshd_config é possivel definir qual user tem permissão de accesso, adicionando: AllowUser <nome-do-user>. Ao tentar acessar qual user que nao esta configurado não terá permissão.

- man sshd_config - abre o manual de configuração ssh

## Rede

O servidor DNS(domain name server) traduz nome para Ips. As configurações estão no arquivo /etc/resolv.conf que mantem o registro dos servidos DNS configurados para serem requisitados pelo dispositivo atual. Utilize tambem o resolv.conf para alterar o servidor dns que ira responder as requisições.

- sudo apt install resolvconf - instala um pacote para tornar um servidor dns de sua preferencia como permanente
- sudo systemctl start resolvconf.sevice - inicia o servico resolvconf
- sudo systemctl enable resolvconf.sevice - habilita o resolvconf para inciar assim que a maquina for ligada.
    - Agora altere o dns no arquivo resolv.conf
- sudo systemctl restart resolvconf.service - reinicia o servico

- ping -c3 8.8.8.8 - envia 3 pacotes para um servidor dns
- ping -w3 8.8.8.8 - define o tempo maximo de de disparos de pacotes para 3
- ping -i0.5 8.8.8.8 - define um intervalo de 0.5 sec entre os disparos

- ip address - lista as interfaces de rede e seus IPs
- iwlist <nome/codigo da rede wifi> scan - mosta a lista de pontos de acesso disponiveis
- sudo nmcli d wifi list - lista as redes sem fio
- nmcli d wifi connect <nome-do-wifi> password <senha> - se conecta a rede wifi
- wget <url> - baixa o arquivo html do site
- head <arquivo-html> - mostra o head do html
- curl <url> - tambem obtem o conteudo de um site

- sudo apt install links - instala um pacote de navegador no console
- nc -v <dominio> <porta> - testa a conexao em um porta especifica

## Processos

top -> Mostra um monitor de processos, ordenado pelos processos que mais utilizam recursos.
ps aux -> lista os processos ativos em execução, juntamente com os PIDs
kill -9 <PID> -> mata o processo pelo pid, -9 é o nivel mais alto de prioridade(força/requisição).
killall -9 <nome-do-processo> -> mata o processo pelo nome
Caractere & -> permite executar um comando em segundo plano. Ex: gedit a.txt &
jobs -> retorna a lista de processos em background
kill %<numero-do-processo> -> Mata o processo em background pelo numero do processo
pkill -> permite filtrar os nomes dos comandos a serem finalizados. Ex:
    - links <url1> & links <url2> & links <url3> &
    - killall -9 links - finaliza todos os processos
    - pkill -9 links - tambem finaliza todos os processos
    - pkill -9 -n - finaliza o ultimo comando
    - pkill -9 -f "links <url1>" - finaliza o processo pelo comando completo
    -
sudo nice -19 <comando> - Define a prioridade de um processo, sendo 19 a prioridade minima e -20 a prioridade maxima
ps ax -o pid,ni,cmd -> verifica a prioridade dos processos existente, filtrando por pid,ni,cmd
sudo renice --20 <PID> -> altera a prioridade de um processo existente, no caso do -20 prioridade maxima.

## Users e groups

stat -c <caminho-arquivo-ou-pasta> -> mostra detalhes sobre um arquivo ou pasta. Use os parametros %U para especificar o user que o arquivo ou pasta pertence, %G para o grupo e %A para o nivel de acesso
find / -group <nome-grupo> | more -> procura por arquivo desde a raiz que pertence a um group. o more permite paginação. Tambem é possivel usar a flag -user para procurar por arquivos que pertencem a um user especifico.
sudo adduser <nome-user> -> cria um novo user com uma iteração perguntando as informações do user.
sudo useradd -m <nome-user> -> cria um user de forma silenciosa. É possivel usar flags para customizar a criação:
    -m : cria o diretorio do user
    -g: define o grupo que o user ira pertencer
    -s: define o shell
sudo usermod -a -G <nome-do-group> <nome-do-user> -> Modifica um user, podendo então adicionar um user a um grupo. É necessario fazer login novamente
sudo usermod -l <novo-nome> <nome-antigo> - permite trocar o login de um user
sudo usermod -d <novo-diretorio> <nome-user> - altera o diretorio do user
groups -> retorna a lista de grupos do user atual faz parte
groups <nome-do-user> -> retorna alista de grupos de um user especifico
users -> retorna os users ativos no sistema
id -> mostra detalhes sobre o user e seus grupos, incluindo o uid, gid, groups
sudo addgroup <nome-do-grupo> -> cria um novo grupo, com interação
sudo groupadd <nome-do-grupo> -> cria um novo grupo, sem interação
sudo groupdel <nome-grupo> -> exclui um grupo
cat /etc/passwd -> mostra os users do sistema
cat /etc/group -> mostra os grupos do sistema
sudo passwd <nome-do-user> -> altera a senha de um user
sudo deluser <nome-do-user> -> remove o user, com interação
sudo userdel <nome-do-user> -> remove o user, sem interação
su <nome-do-user> -> switch user: permite trocar de user
sudo su -> transforma o user atual em root(admin)

## Permissões especiais

bit setuid: permite executar o programa com os privilegios do dono(admin). Um novo caractere é adicionado o 's' nas permissões, permitindo entao qualquer user a executar o arquivo por exemplo
sudo chmod u+s <caminho> -> define o bit setuid
sudo chmod u-s <caminho> -> remove o bit setuid

bit setgid: Arquivos e pastas criados posteriormente terao suas permissoes replicadas dentro do diretorio
sudo chmod g+s <pasta> -> define p bit setgid ma pasta especificada

bit sticky: proteção de arquivos/pastas em diretorios publicos, não permitindo ser deletado
sudo chmod +t <pasta-arquivo> - define o bit sticky

## shell

shell é um programa que controla sistemas operacionais, que pode ser um GUI (graphic user interface) ou CLi(Command line interface)

bash (Bourne Again Shell) é um interpretador de comandos linux, que utiliza um CLI.

~/.bashrc -> arquivo oculto que executa comandos de configuração do terminal ao efetuar um login

alias md='mkdir' -> permiti criar um apelido no terminal, um comando personalizado, nesse caso estou definindo o apelido md para o comando mkdir. O apelido é perdido ao desligar ou reiniciar a maquina, necessitando entao salvar no arquivo .bashrc

shell script é um programa dentro do linux, que executa um script, ou seja, um conjunto de comandos do sistema operacional em um determinada ordem. É utilizado para automatizar tarefas ou personalizar o sistema

chmod +x <nome-arquivo-execução> -> Permite a execução do arquivo

Parâmetros -> Utilizaremos o simbolo $ para trabalhar com parametros:
    - $1 é o primeiro parametro
    - $2 é o segundo parametro ...
    - $* todos os parametros
    - $# retorna a quantidade de parametros

if 'se' -> podemos criar estruturas de decisão. A expressão deve ser definida entre colchetes com espaços antes e depois do codigo dentro dos colchetes
then -> define o conteudo da clausula 'se'
elif -> define o conteudo das demais clausulas 'se'
else -> define o conteudo da clausula 'senão'
fi -> finaliza a estrutura de decisão

Estruturas de decisão literais
==(igual)
!=(diferente)
-n(não-vazio)
-z(vazio)

Estruturas de decisão numericas
-eq(equal)
-lt(less than)
-gt(greater than)
-le(less than or equal)
-ge(greater than or equal)
-ne(not equal)

echo $((1+1)) -> efutua a operação matematica

sistema=`uname` -> armazena o retorno do comando uname na variavel sistema
