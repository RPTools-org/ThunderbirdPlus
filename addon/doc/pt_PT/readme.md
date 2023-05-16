<!--
Por favor, não traduzir ou apagar as 2 etiquetas HTML seguintes:
<br> quebra de linha utilizada nos itens da lista
<um nome=\"un-ID_personnel>: utilizado antes dos títulos listados no índice
Atalhos especiais de teclado, detectados automaticamente pelo addon :
Power 2: Em todas as línguas, o rótulo da tecla por baixo de Tab deve ser preenchido.
igual: a primeira tecla à esquerda do retrocesso deve ser sempre preenchida.
parêntesis direito: preencher a segunda tecla à esquerda do retrocesso.
-->
# ThunderbirdPlus
* Autor: Pierre-Louis Renaud (Thunderbird 78 a 102) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 68 a 91), Yannick (TB 45 a 60) ;
* URL :  [Contacto em inglês e francês](https://www.rptools.org/NVDA-Thunderbird/toContact.html);
* Descarregar a [versão estável][1]
* Descarregar a [Última versão em RPTools.org](https://www.rptools.org/?p=8610)
* Compatibilidade com o NVDA: 2019.3 e superior;
* Compatibilidade com o Thunderbird: versões 102.x ;
* [História das mudanças em RPTools.org](https://www.rptools.org/NVDA-Thunderbird/changes.php?lg=pt_PT)
* [Código fonte no gitHub][2]

Nota: Este extra não é compatível com o extra Mozilla Apps Enhancements. Se tiver instalado este extra Mozilla Apps Enhancements, deverá desactivá-lo ou desinstalá-lo antes de instalar o ThunderbirdPlus ;
<br>

## Descrição
Este extra melhora consideravelmente o conforto e a eficiência da utilização do cliente de correio electrónico Mozilla Thunderbird com NVDA.
As melhorias incluem os seguintes aspectos:

### Conforto auditivo

* Os alertas \"tal pessoa solicitou um aviso de recepção\" podem ser desactivados através de uma opção ;
* Os avisos \"Isto é um rascunho\" e \"o Thunderbird pensa que esta mensagem é fraudulenta\" são simplesmente ignorados;
* Existem opções para desactivar o anúncio de nomes de listas de correio, para remover ou agrupar \"RE\" e para limpar os nomes dos correspondentes através da remoção de números e outros caracteres especiais irritantes;

### Navegação na janela principal

* A passagem para o painel seguinte é feita com a tecla TAB enquanto a tecla de escape é utilizada para regressar ao painel anterior. Isto é mais conveniente do que F6 e Shift+F6.
*  A selecção de separadores com Control+Tab e Control+a número é vocalizada como neste exemplo: Separador 1 de 4, Correio recebido;
* Um atalho de teclado permite listar os separadores num menu para activar facilmente um deles;
* Um atalho de teclado é utilizado para mostrar o menu de contexto da barra de tabulação;

### Árvore de pastas

* alt+ seta para baixo e Alt+ seta para cima para navegar entre pastas com mensagens não lidas;
* A digitação de uma letra ou número selecciona a pasta seguinte cujo nome começa com o carácter digitado. Ao premir a tecla Shift, o movimento é de baixo para cima. Além disso, é anunciado o nome da conta a que a pasta pertence;
* A tecla Espaço numa pasta com mensagens não lidas selecciona a primeira mensagem não lida na lista de mensagens;
* Dois diálogos das contas e as suas pastas associadas permitem filtrá-las por palavra-chave ou mostrar apenas as pastas com mensagens não lidas;

### Lista de mensagens

* A escolha das colunas e a sua disposição na lista de mensagens é tornada acessível através de um diálogo simples;
* Consulta das colunas da lista de mensagens: os atalhos permitem ouvir, soletrar ou copiar facilmente o nome do remetente, o assunto ou a data de uma mensagem, premindo um número no teclado alfanumérico: por exemplo, 1 ou & anuncia o remetente, 2 pressionamentos soletram o nome e 3 pressionamentos copiam-no para a área de transferência;
* Consulta dos cabeçalhos do painel de cabeçalhos apresentado com F8: com Alt+um número, 1 pressionamento indica um cabeçalho contendo os endereços do remetente ou dos destinatários, 2 pressionamentos abrem um diálogo que permite copiá-los, 3 pressionamentos abrem o menu contextual nativo de Thunderbird associado ao cabeçalho;
* Visualização rápida e limpa do texto da mensagem com espaço, Alt+ seta para baixo ou F4: os cabeçalhos de grandes blocos nas citações das mensagens são substituídos pela frase \"O nome do remetente escreveu\". A NVDA anunciará também \"link clicável\" em vez do endereço longo do link.
* Visão rápida das citações em ordem cronológica, de baixo para cima, usando Shift+Espaço, Alt+Up seta ou Shift+F4 ;
* Fácil acesso a anexos com o atalho Alt+ página seguinte ou com o número 1 no teclado alfanumérico;

<!-- Tradutores : tags -->

### Barra de filtragem rápida e gestão de etiquetas prioritárias

* É possível navegar através das opções de filtro usando as setas verticais. A tecla Enter é utilizada para verificar ou desmarcar uma opção;
* as etiquetas são adicionadas ou removidas premindo Shift+um número no teclado alfanumérico. Por exemplo, premir 4 para adicionar a etiqueta \"To Do\" a uma mensagem. A lista de mensagens pode então ser filtrada por etiqueta através da barra de filtro rápido que está agora disponível;

### Janela para escrever uma mensagem

Alt+1 anuncia o Remetente, Alt+2 o Destinatário, Alt+3 os Anexos, etc. Dois pressionamentos colocam o foco num destes campos;

### Diálogo de verificação ortográfica :

* a palavra mal escrita é anunciada com ou sem ortografia antes da palavra sugerida. Os atalhos NVDA+Tab ou seta Alt+up anunciam palavras mal escritas e substituídas: 1 pressionamento soletra as palavras à velocidade normal, 2 pressionamentos soletra-nas rapidamente, 3 pressionamentos copiam a palavra mal escrita para a área de transferência para análise num outro campo de edição;
* várias combinações da tecla enter activam os botões Replace, Replace All, Ignore, Ignore All ou Add Word to Dictionary foram adicionados para maior comodidade a este diálogo;

### Actualização automática

O ThunderbirdPlus tem um sistema independente de actualização automática com opções de desactivação/activação e adiamento;

### Trabalhar em duo com Chichi

O ThunderbirdPlus foi concebido para funcionar em harmonia com Chichi, um add-on que é instalado directamente no Thunderbird.
Leia sobre isto na [página da Chichi](https://www.rptools.org//Outils-DV/thunderbird-chichi-pt.html);

### Sobre línguas

Algumas características não funcionarão correctamente se o ThunderbirdPlus não for traduzido para a língua que utiliza para o NVDA e o Thunderbird.
* os alertas não serão interceptados. Estes incluem projectos de alertas, pedidos de reconhecimento, mensagens fraudulentas, actualizações, etc. ;
* a pesquisa melhorada do Thunderbird não funcionará;
Até à data, a extensão está disponível nas seguintes línguas:
[Versão original em francês](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_fr.html): pelo desenvolvedor ;
Traduções por ordem de antiguidade :
* [Português](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_pt_PT.html): por Ângelo Abrantes e Rui Fontes membros da equipa portuguesa do NVDA;
* [Espanhol](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_es.html) : por Rémy Ruiz ;
* [Inglês](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_en.html) : por Bachir Benanou ;

Agradecimentos aos tradutores.

## Navegar entre painéis na tabulação de mensagens (Tab, Escape)

Este é o separador que contém os seguintes painéis: a árvore de pastas, a lista de mensagens e o cabeçalho e painel de pré-visualização de mensagens (mostrado ou oculto com a tecla F8).   

* TAB: passar para o painel seguinte. Este atalho será mais ergonómico para alguns do que F6 ;
* Fuga: regresso ao painel anterior. Equivalente a Shift+F6 ;

Nota:
Quando se separa da lista de mensagens para chegar ao texto, a área de cabeçalhos é saltada. Para chegar a esta área de cabeçalho, prima Alt+1 número do teclado alfanumérico três vezes rapidamente e depois Escape para sair do menu de contexto do cabeçalho.  Estes atalhos Alt+dígito reduzem a necessidade de ir para a área do cabeçalho. Para mais detalhes, ver a secção \"Ver cabeçalhos\" abaixo.  

<a name=\"threadTree\">

## Lista de mensagens, painel de pré-visualização e janela de reprodução separada

Alguns dos seguintes atalhos são comuns aos três contextos, outros são específicos do contexto.

<a name=\"attach\">

### Acesso a anexos (Alt+Página seguinte)
* Alt+ página seguinte ou Alt+p: se o painel de pré-visualização for mostrado (via F8), abre a lista de anexos da mensagem seleccionada;
* Alt+9 ou o número 1 ou 2: apenas a partir da lista de mensagens, um pressionamento indica o número de anexos, dois pressionamentos abrem a lista de anexos;

<a name=\"readPreview\">

### Leitura rápida e desordenada de mensagens
* Os comandos para ler rapidamente uma mensagem estão disponíveis em três contextos: a partir da lista de mensagens, a partir de uma mensagem aberta numa tabulação ou numa janela separada;
* Todos eles são agora compatíveis com mensagens de Framalistes;
* A maioria dos atalhos de leitura rápida do teclado foram focados na minimização do movimento das mãos durante uma sessão de leitura de mensagens múltiplas;
* Uma única pressão na tecla principal de um atalho inicia a leitura limpa da mensagem, ou seja, com os cabeçalhos das aspas fortemente encurtados.
* Pressionar duas vezes começará a ler a mensagem na sua forma original. O termo \"leitura não filtrada\" é sinónimo de ;

<a name=\"readFromList\">

#### Ler rapidamente mensagens 'da lista sem sair da mesma (Espaço, F4 ou Alt+ seta para baixo)

Para tirar partido desta funcionalidade, deve primeiro mostrar o painel de mensagens com a tecla F8. Ao premir esta tecla, ouvirá se este painel está presente ou ausente;
Depois ir para a lista de mensagens e utilizar as seguintes teclas:
* Espaço, Alt+Down Arrow ou F4: ler o corpo da mensagem sem sair da lista. Depois de ler uma mensagem, pressionar a seta para baixo, depois a seta Espaço ou Alt+Seta para baixo ou F4 para ouvir a mensagem seguinte;
* Clicando duas vezes, aparece a lista de links na mensagem se Chichi estiver activa. Se for seleccionado um artigo RSS feed, este será aberto no navegador da web;
* Shift+espaço, Alt+Up ou Shift+f4: o mesmo que acima, mas lê as citações por ordem cronológica (de baixo para cima);
E para completar os comandos disponíveis a partir da lista de mensagens, citamos aqui :
* letra n ou Alt+Seta Direita: selecciona a próxima mensagem não lida, mesmo através de pastas;
* Alt+Página seguinte ou Alt+p da lista de mensagens: permite-lhe ir directamente para a área de anexos, sem ter de tabular através do texto;

<a name=\"readFromWinTab\">

### Ler rapidamente uma mensagem numa janela separada ou separador de mensagem (F4 ou Alt+Seta para baixo)

Quando uma mensagem é aberta numa nova janela, o corpo da mensagem é automaticamente lido por defeito. No entanto, os atalhos seguintes permitem-lhe ouvir a mensagem novamente em qualquer altura.
* F4 ou Alt+ seta para baixo: leitura rápida do corpo da mensagem;
* Shift+F4 ou Alt+seta para cima: a mesma mas em reverso;
Observações :
* Como lembrete, uma dupla pressão sobre estes atalhos irá ler a mensagem original;
* A reprodução automática pode bloquear o NVDA em alguns PCs, especialmente se a conta for configurada para IMAP. Para tentar resolver este problema, o atalho Alt+d abre uma caixa de entrada que permite prolongar o tempo entre a abertura da janela e o início da reprodução automática;<br>
Se a definição deste atraso não resolver o problema, pode desactivar esta leitura automática através do menu [Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab) / Options for the main window / separate reading window: não ler automaticamente a mensagem se esta causar bloqueios NVDA;
* Para aproveitar ao máximo a experiência de leitura limpa e ao mesmo tempo proteger-se do conteúdo remoto que não respeita a sua privacidade, mostrar o corpo da mensagem em HTML simples. Para o fazer, abra o menu Ver, desça para o Corpo da Mensagem e no sub-menu, valide a opção HTML Simples.
Visualização de colunas e cabeçalhos :
Deve ser feita aqui uma distinção entre colunas e cabeçalhos: a palavra \"coluna\" é utilizada abaixo para se referir ao valor de uma célula numa linha na tabela de mensagens. A palavra \"cabeçalho\" refere-se à própria mensagem. Os cabeçalhos podem ser visualizados tanto no painel de pré-visualização da mensagem como no separador ou janela separada de uma mensagem aberta;

<a name=\"readCols\">

### Consulta das colunas: um dígito do teclado alfanumérico
Estas teclas são apenas para as colunas da lista de mensagens. Prima um número no teclado alfanumérico sem premir a tecla Shift:
* Um único toque: indica o nome e o valor da coluna correspondente;
* Carregue duas vezes num número: escreva o valor da coluna correspondente;
* Três pressionamentos rápidos: copiar o valor da coluna para a área de transferência. Para copiar os endereços dos vários remetentes e destinatários, utilizar a pesquisa de cabeçalho vista abaixo;

<a name=\"readHeaders\">

### Visualização dos cabeçalhos : Alt+número do teclado alfanumérico

Estes atalhos podem ser utilizados a partir da janela principal se o painel de pré-visualização for mostrado (via F8) e a partir do separador ou da janela separada de uma mensagem aberta. Um pressionamento mostra o cabeçalho e dois pressionamentos mostram um menu contextual, conforme o caso;
* Alt+1: anuncia o nome do remetente e o seu endereço de e-mail, dois pressionamentos abrem uma caixa para editar estes valores. Pode editá-los e depois premir Enter para os copiar para a área de transferência. 3 pressionamentos: abre o menu de contexto do cabeçalho;
* Alt+2: Assunto com o nome da lista de correio, se aplicável ;
* Alt+3: data da mensagem ;
* Alt+4 para: destinatários principais da mensagem, se mais do que um destinatário, 3 pressionamentos posicionam o foco no primeiro destinatário, então o separador permite ir para o próximo, aplicações em cada destinatário exibe o menu contextual;
* Alt+5 : Com cópia;
* Alt+6 : Destinatários das cópias ocultas ;
* Alt+7 : endereço \"responder a\" ;
* Alt+8: utilizador, se os cabeçalhos completos forem activados através do menu Ver / Cabeçalhos / Completo;
* Alt+9: 1 pressionamento anuncia o número de anexos, 2 pressionamentos abrem a lista de anexos;
* Alt+0: lista de etiquetas prioritárias colocadas na mensagem ;
* Alt+ [Apóstrofo](keyEquiv_pt_PT.html#bs2) ou Alt+end: indica uma versão abreviada da barra de estado: número de mensagens não lidas, número total de mensagens e a expressão do filtro rápido ;
* Alt+ [abre aspas](keyEquiv_pt_PT.html#bs1) : abre o menu contextual dos separadores ;
* Controlo + [abre aspas](keyEquiv_pt_PT.html#bs1) :  Apresenta a lista de separadores abertos num menu que lhe permite seleccionar o separador escolhido;

<a name=\"tags\">

### Adicionar e remover etiquetas prioritárias: Shift+um número no teclado alfanumérico

Esta característica permite-lhe marcar uma mensagem como importante ou a fazer, por exemplo. Depois, a barra de filtro rápido mostrará apenas mensagens com uma ou mais etiquetas. Por exemplo, exibirá apenas mensagens importantes na lista de mensagens;
Para verificar as etiquetas já colocadas na mensagem, prima Alt+0 no teclado alfanumérico.
Para adicionar ou remover uma etiqueta, prima Shift+ um número de 1 a 9 ;

<a name=\"qfb\">

### Barra de filtro rápido (letra f ou Control+Shift+K)

* letra F ou Control+Shift+K: mostra a barra de filtro de mensagens rápidas na pasta actual;
* Filtragem por palavra-chave: introduzir uma palavra-chave e depois premir Tab para navegar na lista filtrada com as setas;
* A seta para baixo do campo de introdução de palavras-chave dá-lhe acesso à lista de opções abaixo:
    * 1: Manter filtros ao trocar de ficheiros c
    * 2: Mostrar apenas mensagens não lidas l
    * 3: Mostrar apenas mensagens rastreadas
    * 4: Mostrar apenas mensagens de pessoas na minha agenda de endereços de
    * 5: Mostrar apenas mensagens com etiquetas
    * 6: Mostrar apenas mensagens com anexos j
    * etc.
* Prima enter para activar ou desactivar um ou mais destes critérios;
* Alt+end ou Alt+[abre aspas](keyEquiv_pt_PT.html#bs1): reproduz um resumo dos filtros activos e o número de mensagens filtradas. Ambos estes atalhos também funcionam a partir da lista de mensagens, não apenas a partir da barra de filtros rápidos;
- quando um filtro rápido está activo, um ficheiro áudio WAV é reproduzido quando a lista ou o separador a que pertence recebe o foco. O som assemelha-se a uma respiração;<br>
O ficheiro filter.wav está localizado na pasta<br> 
\"%appdata%\\NVDA\\TB+sounds\" <br>
Pode colocar nele um som à sua escolha desde que o seu ficheiro seja chamado: filter.wav. Após esta alteração, terá de reiniciar o NVDA ;v

<a name=\"tagFilter\">

#### Filtragem por Etiqueta

quando o foco é colocado na área de edição da barra de filtragem rápida :
*  Prima a seta para baixo até ouvir \"etiquetas\" e depois prima Enter para assinalar esta opção;
*  Em seguida, prima a tecla Tab para ir para a lista pendente de modos de filtragem por etiqueta. Por exemplo, se escolher \"a fazer\", apenas as mensagens etiquetadas como \"a fazer\" serão listadas na tabela de mensagens;

<a name=\"colLayout\">

### Disposição das colunas (Alt+c)

O atalho Alt+c exibe um diálogo que lhe permite alterar a ordem das colunas na lista de mensagens e adicionar ou remover colunas.
Para utilizá-lo, primeiro vá à lista de mensagens ou à árvore de pastas e prima Alt+c ;
Aparece o diálogo de disposição das colunas. É constituído pela lista de colunas e pelos botões \"Ajuda\", \"Colunas\" e \"Fechar\".
O botão \"Colunas ...\" mostra o menu nativo de Thunderbird \"Escolher colunas para mostrar\"
Quando estiver na lista de colunas, estão disponíveis os seguintes atalhos de teclado:
* Seta à esquerda: mostra o menu da caixa de verificação chamado \"Escolha as colunas a mostrar\". Este atalho corresponde ao botão \"Colunas ...\";
* Espaço: Para mover a coluna seleccionada, prima Espaço, depois mova-se para outra coluna e prima Espaço novamente para mover a coluna para lá. Isto é semelhante ao corte e colagem;
Também tem estes atalhos de deslocação directos:
* Controlo + seta para cima ou para baixo: move a coluna seleccionada para cima ou para baixo uma posição;
* Controlo + Início ou Fim: move a coluna seleccionada para cima ou para baixo na lista;
* Controlo + Página para cima ou página para baixo: move a coluna seleccionada para cima ou para baixo três posições;
Para fazer estes movimentos, as colunas são realmente movimentadas arrastando e largando com o rato.  Um sinal sonoro de um milissegundo ocorre a cada 10 movimentos do ponteiro;
Quando o menu \"Escolher colunas a mostrar\" está presente, estão disponíveis os seguintes novos atalhos de teclado:
* Seta para a direita: mostra o diálogo de disposição das colunas;
* Espaço: Verifica ou desmarca a coluna seleccionada no menu. A tecla Enter continua a produzir o mesmo comportamento;
Com as setas esquerda e direita, é portanto muito fácil alternar entre o menu para escolher colunas e o diálogo para as organizar;

<a name=\"smartReply\">

### SmartReply: responder a todas as listas de correio pressionando Control+r
Se for uma daquelas pessoas que se esquece de carregar em Control+Shift+l para responder a uma lista de correio como o GoogleGroups, esta funcionalidade impedi-lo-á de responder em privado ao remetente de uma mensagem sem se aperceber disso.
pode sempre premir Control+r como se segue:
* digitando: para responder à lista ;
* double-tap: para responder em privado ao remetente da mensagem;
* um único toque de tecla para responder ao remetente de uma mensagem não proveniente de uma lista;
Observações :
A distinção entre pressionamento simples e duplo nestes atalhos funciona no GoogleGroups, Framalistes e FreeLists.
Com uma única pressão numa destas três listas, ouvirá \"para a lista\" antes de abrir a janela de edição.
é também aconselhável não utilizar o comando \"Responder a todos\" para responder a uma lista, para que o remetente não receba a sua resposta em privado;
E finalmente, se desejar regressar ao comportamento habitual de Control+r :
* Prima [Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab) para mostrar o menu Opções;
* Seleccione \"Desactivações para Chichi e para Thunderbird+ sub-menu\" ;
* Prima Enter para desmarcar \"Lista de mensagens: sem resposta SmartReply\";

### Atalhos a, j, m vocalizados

* a : Arquivar a mensagem seleccionada, com vocalização. Pressione Control+z para cancelar esta operação;
* j: marca esta mensagem como não desejada, com vocalização ;
* Shift+j: marca esta mensagem como aceitável, com vocalização ;
* m: marca as mensagens seleccionadas como não lidas. Shift+m marca-as como lidas;

<a name=\"folderTree\">

### Árvore de pastas

<a name=\"unreadFolders\">

### Navegação rápida entre pastas contendo mensagens não lidas (Alt+Seta para baixo, Alt+Seta para cima)

Quando estiver na árvore de pastas, pode premir :
* Alt+ seta para baixo: para ir para a pasta seguinte com mensagens não lidas;
* Alt+ seta para cima: para ir para a pasta anterior com mensagens não lidas;
* Espaço, Desinstalado Chichi: Se a pasta seleccionada contiver mensagens não lidas, selecciona a primeira mensagem não lida da lista;
* Espaço, Chichi instalado: o mesmo excepto que se a pasta não tiver mensagens não lidas, Chichi irá mostrar a lista de pastas não lidas.<br>
Ao pressionar enter numa pasta não lida desta lista, a primeira mensagem não lida nessa pasta será activada na lista de mensagens; <br>
Isto permite-lhe rever rapidamente as pastas que receberam mensagens antes de decidir qual delas começar a ler;<br>
Nesta linha, ver também estes dois diálogos:
* Diálogo de Listas Filtradas de Contas e Pastas (F12)
* Lista de pastas na árvore principal, em 4 tipos (F7, NVDA+F7 ou Shift+F12)
Nota: com um grande número de pastas, Chichi é instantânea, ao contrário destes dois diálogos;

<a name=\"folderDlg\">

### Diálogo de Listas de Contas e Pastas Filtradas (F12)
Este diálogo mostra as contas e as suas pastas associadas em duas listas separadas. Pode filtrá-las por uma palavra-chave ou restringir a lista de pastas às pastas com mensagens não lidas.
Definir o modo de visualização por defeito :
Se pretende verpastas com mensagens não lidas apenas na maioria das vezes, primeiro vá à árvore de pastas ou à lista de mensagens, prima o atalho [Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab) e no submenu de opções da janela principal, active o item intitulado: ver apenas pastas com mensagens não lidas
Utilização básica do diálogo :
* A partir da janela principal, premir F12 para mostrar o diálogo.
* Se tiver configurado a exibição padrão de pastas com mensagens não lidas, estas serão exibidas na lista chamada: pastas de contas ;
* Caso contrário, todos os registos de todas as contas serão incluídos nesta lista;
* Pode mover-se através desta lista premindo a primeira letra de um nome de pasta;
* Note-se que as pastas que não são mostradas na vista em árvore também não serão listadas aqui. Isto acontece, por exemplo, quando as pastas pertencem a uma conta reduzida na árvore de contas e pastas;
* Se encontrou a pasta que lhe interessa neste momento, prima Enter para a seleccionar na árvore.  Pode também premir Alt+g para simular um único clique esquerdo na pasta ou Alt+d para simular um único clique direito;
Mudança dos modos de visualização :
* Para se lembrar em qualquer altura em que modo de visualização se encontra, prima a tecla \"Backspace\". Depois de ouvir a informação, prima novamente esta tecla para voltar à lista de pastas;
* Para mudar a visualização de \"apenas com pastas não lidas\" para \"todas as pastas\" e vice versa, prima F12 ;
* No modo \"todas as pastas\", as contas são mostradas na lista da esquerda e as pastas da conta seleccionada na lista da direita. Para mudar de uma lista para a outra, utilizar as setas esquerda e direita ;
* uma conta virtual chamada \"Todas as contas\" é seleccionada e o foco é colocado na lista de pastas que inclui todas as pastas de todas as contas. Em cada pasta desta lista, é mencionado o nome da conta a que pertence;
Utilização de filtragem por palavra-chave :
* Antes de o fazer, é provavelmente uma boa ideia mudar para o modo \"Todas as pastas\", como explicado acima;
* Em baixo, pode utilizar as teclas \"Page Up\" ou \"Page Down\";
* A partir de uma lista, prima a tecla \"Página anterior\" para voltar ao campo de edição da expressão do filtro;
* Introduza uma expressão e valide-a com o botão \"Página seguinte\" para executar a filtragem;
* Os resultados são apresentados na lista de pastas. Se nenhum ficheiro for encontrado, ouvirá : Nenhum resultado. Se não estava à espera disto, pode ter-se esquecido de mudar para o modo de exibição de todas as pastas;
-Finalmente, prima enter na pasta desejada para a seleccionar na árvore de pastas. Como mencionado acima, pode simular um clique esquerdo ou direito sobre a pasta, premindo Alt+g ou Alt+d ;

#### Excluir algumas pastas da lista de pastas com ficheiros não lidos

Como mencionado acima, pode excluir raramente ou nunca as pastas da lista de pastas com mensagens não lidas.
Isto é feito renomeando uma pasta a ser excluída, acrescentando um traço ao fim do seu nome.
É necessário salientar aqui que se esta pasta renomeada fizer parte de um filtro de mensagens, Thunderbird modificará automaticamente este filtro para ter em conta esta alteração

<a name=\"foldersList\">

### Lista de pastas na árvore principal, por 4 tipos (F7, NVDA+F7 ou Shift+F12)

Quando estiver na árvore de pastas ou na lista de mensagens, este comando mostra um diálogo com uma lista de pastas que pode assumir as quatro formas seguintes:
* Apenas com mensagens não lidas (lista plana), Alt+n ;
* Todas as pastas (lista plana), Alt+t ;
* Apenas com mensagens não lidas (árvore completa), Alt+o ;
* Todas as pastas (árvore completa), Alt+u ;
Para pastas com mensagens não lidas, as pastas de rascunho, Trash e Hyphenated estão excluídas da lista;
Para activar um destes tipos, pode premir o atalho de teclado associado ou Shift+Tab e depois as teclas de seta para alterar o modo.
O tipo seleccionado será guardado e activado na próxima vez que este diálogo for mostrado;
Também é possível filtrar a lista por palavra-chave. Prima Tab ou Alt+e vazio para chegar ao campo de entrada.
A navegação numa lista plana ou estrutura em árvore é feita com as setas para cima e para baixo e pela inicial de um nome de pasta;
Para activar a pasta seleccionada na árvore principal, basta premir Enter nela.
Dica: Se tiver premido Enter numa pasta com mensagens não lidas, então prima Espaço para seleccionar a primeira mensagem não lida na tabela de mensagens;
Nota:
Os atalhos de teclado que mostram este diálogo podem ser eliminados e outro adicionado através do diálogo gerir Comandos do NVDA. Proceder como se segue:
* Primeiro, trazer a janela Thunderbird para o primeiro plano;
* Abrir o menu do NVDA e seleccionar \"Preferências\";
* No sub-menu, clique em : \"definir comandos\";
* No diálogo, prima a letra t até ouvir: Thunderbird ;
* Prima a seta para a direita para expandir este ramo;
* Desça até ao item: \"Mostrar a lista de pastas na árvore principal do Thunderbird, de acordo com vários tipos. reduzido 2 de 4 nível 1\" e depois prima a seta para a direita para expandir este nível;
* Tab até ao botão \"Adicionar\", e depois pressionar um atalho no novo diálogo;
* Prima Enter para confirmar a sua escolha;
* De volta à lista de atalhos, verifique o seu novo atalho;
* Fechar o diálogo através do botão OK.

<a name=\"alerts\">

## Alertas acessíveis

Para alertas que requerem a sua intervenção, os botões são acessíveis e a navegação entre eles pode ser feita com as setas do teclado:
* instalação de módulos para o Thunderbird: o botão \"Instalar\" é seleccionado e só tem de premir Enter para continuar a instalação;
* Nova actualização Thunderbird: este alerta também está disponível;
* Pedido de reconhecimento de mensagem: isto pode ser ignorado através de uma opção de menu [Shift+Barra invertida] (keyEquiv_pt_PT.html#aboveTab) / opções para a janela principal;
* Bloquear a exibição do conteúdo remoto nas mensagens: o botão \"Opções\" é seleccionado e a seguinte frase é adicionada à mensagem: Dica: Abra o menu Ver, desça até ao corpo da mensagem e valide o HTML simples no submenu. Ao aplicar as configurações propostas, este alerta deixará de ser mostrado;
Para alertas que interferem com o fluxo da lista de mensagens :
* Alerta Este é um rascunho: este alerta desnecessário é eliminado;
* Thunderbird pensa que esta mensagem é fraudulenta: este anúncio é substituído por dois tons curtos de uma frequência próxima da voz humana (200 Hertz). Para tornar a mensagem aceitável ou indesejável, prima a tecla [Barra invertida] (keyEquiv_pt_PT.html#aboveTab) e seleccione a acção desejada no submenu \"Alerta\";

<a name=\"tabs\">

## Atalhos de teclado para separadores

Para além dos novos comandos, são anunciados separadores como neste exemplo: Separador 1 de 4, Correio recebido.
* Control+Tab e Control+Shift+Tab: vai para o separador seguinte ou anterior;
* Controlo+um número: selecciona o separador correspondente ao seu número na barra de separadores.  Se premir um número superior ao número de separadores abertos, será colocado no último separador;
* Control + [abre aspas](keyEquiv_pt_PT.html#bs1): mostra uma lista de separadores abertos num menu. Prima enter num nome de separador para avançar para o mesmo;
* Alt + [Abre aspas](keyEquiv_pt_PT.html#bs1) : mostra o menu contextual da barra de tabulação. Inclui os comandos: Fechar o separador activo e Fechar os meus outros separadores;
* Control+w, Control+backspace ou Control+F4: fecha o separador activo;
* Control+j: abre o separador \"Ficheiros guardados\", que contém anexos e downloads guardados no seu disco rígido;

<a name=\"tabAddons\">

## Separador de extras

A extensão torna fácil encontrar e instalar add-ons para o Thunderbird.
* No separador \"extras\", introduza um nome de módulo e prima Enter ;
* A extensão aguardará a abertura do separador de resultados da pesquisa e depois tentará seleccionar o primeiro add-on encontrado;
* mais concretamente, pode ler o exemplo de [a instalação do módulo Start With Inbox](#stwInstall) ;

<!-- Tradutores: Write window -->
<a name=\"writeWnd\">

## Janela de edição

Quando a janela de edição se abre, nada de especial é perceptível, embora estejam disponíveis os seguintes atalhos de teclado:
* Escapes: fecha a janela de edição;
* Consulta das zonas de endereçamento: um pressionamento em Alt + um número anuncia o cabeçalho, dois pressionamentos dão o foco para a zona de entrada correspondente:<br>
Alt+1: Remetente: um dos seus endereços de correio electrónico da lista dos seus endereços de correio electrónico;<br>
Alt+2 : para :<br>
Alt+3: os nomes dos anexos. Duas prensas dão destaque à lista de anexos;<br>
os outros números dão acesso a cabeçalhos opcionais tais como: cópia para, cópia oculta para e resposta a;
* [Barra invertida](keyEquiv_pt_PT.html#aboveTab) no texto da mensagem: mostra o seguinte menu de contexto: - Barra de ferramentas de correio no sub-menu: Enviar, Ortografia, Anexar, Segurança, Guardar.<br>
Formatação de texto então no submenu: (Estilos de) Parágrafo, Aplicar ou remover uma lista numerada, Aplicar ou remover uma lista numerada, Fontes, Indents, inserir um link, uma imagem, uma âncora, uma linha horizontal ou uma tabela. 
Nota: Este menu é obtido premindo [Barra invertida](keyEquiv_pt_PT.html#aboveTab) uma ou duas vezes, dependendo da configuração no menu de opções da janela de edição obtida premindo [Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab) rapidamente uma ou duas vezes;

<a name=\"spellDlg\">

## Diálogo de verificação ortográfica: F7 

Foram acrescentados atalhos de teclado que restringem o movimento das mãos. Quando o foco é colocado no campo de edição da palavra de substituição, é possível premir os seguintes atalhos de teclado:

* Input: Activa o botão \"Replace\" (Substituir);
* Shift+Enter: Activa o botão \"Replace All\" (Substituir tudo);
* Control+Enter: Activa o botão \"Ignorar\";
* Shift+Control+Enter: Activa o botão \"Ignorar Tudo\";
* Alt+Enter: Activa o botão \"Adicionar palavra ao dicionário\";

Para recordar estas combinações da tecla Enter, Controlo refere-se à acção \"Ignorar\" e a presença de Shift indica \"todas as ocorrências\".
Além disso, o atalho de seta Alt+up soletra as palavras :

* 1 pressionamento soletra as palavras a um ritmo normal;
* 2 pressionamentos Soletra as palavras rapidamente;
* 3 pressionamentos copiam a palavra mal escrita para a área de transferência para análise noutro campo de edição;

<a name="virtspell">

## Modo de verificação ortográfica avançada durante a digitação
Apesar da ortografia adicionada ao diálogo de verificação ortográfica, é por vezes necessário fechar o diálogo para ouvir o contexto do erro no texto. Quando isto é feito, o diálogo recomeça desde o início e pára novamente nas palavras que anteriormente eram ignoradas.

A correcção ortográfica durante a digitação evita estes inconvenientes mas pode distrair o escritor com os anúncios de "erro ortográfico". 
A fim de não se distrair com erros ortográficos durante a escrita, este modo de verificação foi melhorado com a adição de três atalhos de teclado:

B antes de os activar, é necessário mudar para o modo de navegação pressionando ;: NVDA+espaço ;

* w e Shift+w para ir para o erro seguinte ou anterior, respectivamente, ;
* NVDA+F7 para exibir a lista de erros. Basta pressionar enter sobre um erro para se mover para ele no texto;

Este modo de funcionamento permite-lhe desactivar o anúncio de erros ortográficos pelo NVDA ;

Antes de utilizar este modo melhorado de verificação durante a digitação, é necessária uma pequena quantidade de configuração.

### Configuração preliminar
1: Nas preferências do Thunderbird, permitir a verificação ortográfica enquanto se escreve:

* Na janela principal, abrir o menu Ferramentas, ir para baixo até Settings e confirmar;
* No separador Settings, no campo de opções de pesquisa, introduza a palavra "ortho" e pressione Tab ;
* Nos resultados, Tab até "Verificar ortografia ao escrever" e marcar com barra de espaços, se necessário;
* Finalmente, feche o separador Preferências com Control+w.

2: Desactivar o anúncio de erros ortográficos no NVDA
Esta configuração é, evidentemente, opcional. Se preferir ouvir um anúncio sobre um erro ortográfico, também pode encurtar este anúncio substituindo no seu dicionário de pronúncia "Erro ortográfico" por "graf", por exemplo ;

Para desactivar este anúncio :

* Abrir o menu NVDA, Preferências e depois validar em : Configurações ;
* No diálogo de Configurações, ir para a categoria "Formatação de documentos";
* Tab até ouvir: "Erros ortográficos" e depois pressione espaço para desmarcar esta opção;
* Fechar o diálogo pressionando o botão OK ou Confirmar;

### Utilizando os comandos w, Shift+w e NVDA+F7

* Antes de utilizar estes atalhos, deve primeiro activar o modo de navegação, pressionando NVDA+espaço;
* Em seguida, pressione a letra w para passar ao erro seguinte ou Shift+w para passar ao erro anterior ou pressione NVDA+F7 para seleccionar a palavra a ser corrigida a partir de uma lista;
* Quando a palavra errada é seleccionada no texto, pode pressionar a tecla Aplicações para exibir o menu contextual de sugestões de substituição; 
* Também se pode ouvir facilmente a frase que contém a palavra errada antes de a corrigir;
* Para fazer uma correcção manual a uma palavra, primeiro pressione NVDA+espaço para voltar ao modo formulário;

<a name=\"menus\">

## Opções do ThunderbirdPlus e menus de comandos 

<a name=\"optMenu\">

### Menu de Opções([Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab)) 

$$518
Opções para a janela principal 
* Agrupar múltiplas declarações 'RE' em uma: por exemplo Re: Re: Re: será transformado em 3Re: ;
* Eliminar o 'RE' na coluna de assunto:
Eliminar os dois pontos no texto 'RE', 
* Limpa os nomes dos correspondentes na lista de mensagens: remove números e alguns caracteres especiais para tornar a audição dos nomes dos correspondentes menos cansativa;
* Adicionar pontuação entre colunas: uma vírgula é adicionada entre algumas colunas para marcar uma pequena pausa entre elas quando se anuncia uma linha na lista de mensagens;
* Ocultar nomes de listas de correio: remove o anúncio de nomes de listas entre parênteses rectos ou chaves para uma audição mais confortável quando se utiliza uma pasta diferente para cada lista de correio. Caso contrário, um nome de lista de correio só é anunciado uma vez se aparecer mais de uma vez na linha de assunto de uma mensagem; 
* Editar palavras a esconder no assunto da mensagem: abre uma caixa de entrada que lhe permite adicionar ou remover palavras que não devem ser anunciadas no assunto da mensagem. Por exemplo, adicionar * para que *** Spam *** seja anunciado como Spam ;
* Anunciar 'Indesejado' se for apresentada na coluna 'Estado Indesejado': se a coluna 'Estado Indesejado' estiver presente na tabela de mensagens, esta opção permite ou não anunciar 'Indesejado';
* Espaço numa pasta com pesquisas por ler para a primeira mensagem não lida desde o início da lista de mensagens: Por defeito, o script para esta opção envia o comando \"n\" para seleccionar a próxima mensagem não lida na lista de mensagens. O Thunderbird não selecciona necessariamente a primeira mensagem não lida na lista. Ao marcar esta opção, a extensão seleccionará a primeira mensagem não lida na pasta fazendo um desvio que pode ser ouvido em alguns PCs;
* Não utilizar a navegação por letra inicial na árvore de pastas: esta opção é útil se utilizar o add-on \"Navegação rápida de chaves de pastas\";
* Navegação Inicial Indirecta: Apresenta uma caixa de introdução de nome de pasta sempre que premir uma letra ou número na árvore de pastas. Se esta opção estiver desactivada, pode mostrar esta caixa de pesquisa premindo a letra z ; 
* Ignorar pedidos de reconhecimento: Se esta opção estiver activada, o painel de pedido de reconhecimento será ignorado quando uma mensagem for seleccionada na lista de mensagens;
* Não emular Shift+F6 com escape: desactiva o uso da tecla de escape quando se navega entre painéis na janela principal; 
* Mostrar apenas pastas com mensagens não lidas na caixa de diálogo 'Pastas em árvore: permite-lhe mostrar apenas pastas com mensagens não lidas cada vez que mostrar este diálogo através da tecla F12;
* janela de leitura separada: não ler automaticamente a mensagem se esta causar bloqueios no NVDA: Por defeito, quando uma mensagem é aberta premindo Enter da lista de mensagens, é iniciada uma leitura limpa da mensagem quando a nova janela é aberta. Em alguns computadores e quando a conta de correio electrónico está definida para IMAP, a NVDA pode bloquear-se a si própria. Quando esta opção é verificada, esta leitura automática é desactivada para evitar o bloqueio.<br>
Se verificar que esta janela não se abre, pode prolongar o tempo antes do início da reprodução automática. Para o fazer, prima Alt+d para introduzir outro valor. Se não conseguir remover o congelamento, então marque esta opção; 
Opções para a janela de edição 
* Verificação ortográfica: soletra a palavra mal escrita e a palavra sugerida: esta opção altera os anúncios no diálogo de verificação ortográfica;
* Activar a Verificação Ortográfica Avançada durante a digitação: o comando para esta opção ainda não funciona na versão NVDA 2022.1;
* A tecla Escape fecha a mensagem que está a ser escrita; verifique a
* Um toque para mostrar o menu contextual, duplo toque para escrever [Barra invertida](keyEquiv_pt_PT.html#aboveTab) ou [Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab) ou os seus substitutos: esta opção permite mostrar o menu contextual digitando [Barra invertida](keyEquiv_pt_PT.html#aboveTab).html#aboveTab), que será mais prático se escrever muito raramente os caracteres [Barra invertida](keyEquiv_pt_PT.html#aboveTab) e [Shift+Barra invertida](keyEquiv_pt_PT.html#aboveTab) ;
Opções de actualização :
Esta opção permite-lhe desactivar ou reactivar actualizações automáticas para Thunderbird+;
Desactivações para Chichi e Thunderbird+ :
O principal objectivo destas opções é permitir uma boa coabitação entre Thunderbird+ e Chichi, evitando a duplicação de características. Mas pode utilizá-las sem Chichi para se adequar às suas preferências;
O termo \"pastas\" abaixo refere-se à árvore de pastas;
* Pastas: O espaço não selecciona a próxima mensagem não lida na lista e não mostra a lista de pastas não lidas d: Chichi ainda não tem um equivalente autónomo;
* Pastas: sem navegação por iniciais d: ao activar esta opção, Chichi será utilizado.  Só funciona de cima para baixo e não indica o nome da conta a que a pasta activada pertence; 
* Lista de mensagens: O espaço não lê a mensagem do painel de pré-visualização l: Se marcar esta opção, Chichi lerá a mensagem do painel de pré-visualização. Ao contrário do Thunderbird+, esta leitura não será limpa. Em vez disso, F4 e Alt+Down Arrow continuarão a utilizar a leitura limpa do Thunderbird+; 
* Lista de mensagens: sem SmartReply: desactiva a funcionalidade que lhe permite responder a uma lista de correio com Control+r toque simples ou ao remetente com Control+r toque duplo,
* Lista de mensagens: não gerir a barra de filtro rápido: remover o acesso às opções de filtro com a seta para baixo ;
* janela principal: Tab não se move para o painel seguinte: esta opção é para navegar entre a árvore de pastas, a lista de mensagens e o cabeçalho e painel de mensagens;
* Janela principal: restaurar o comportamento por defeito da tecla escape. Isto aplica-se em particular à navegação entre os painéis acima mencionados;
* Permitir fechar o Thunderbird com Control+w ou Control+F4: marcando esta opção, estes dois atalhos fecham o Thunderbird quando apenas um separador é deixado aberto. Este comportamento é irritante para algumas pessoas;
Opções de poupança e restauro :
* Guardar configurações actuais s: copiar o ficheiro .ini da extensão para um ficheiro .inibak;
* Restaurar configuração guardada r: copia o ficheiro .inibak para o ficheiro .INI e carrega novamente as definições;
* Repor a configuração r: recarrega as configurações padrão da extensão. Antes de o fazer, faça uma cópia de segurança se ainda não existir uma;

<a name=\"cmdMenu\">

### Menu de controlos (Barra invertida) 

* Escolher e organizar colunas na lista de mensagens: Apresenta o menu da caixa de verificação Thunderbird chamado \"Escolher colunas a apresentar\". A partir do nome de uma coluna, prima a seta para a direita para abrir o diálogo de disposição das colunas;
* Escrever para o suporte: em inglês ou francês. Este comando abre uma janela pré-endereçada de escrita de apoio para a extensão. Isto só funciona se o Thunderbird estiver correctamente configurado como o seu cliente de email predefinido;

<a name=\"startup\">

## Arranque melhorado do Thunderbird

Nativamente, após o último fecho do Thunderbird, começa no último separador activo e sem nada activado, o que é bastante desagradável.
Para obter um início confortável, existem dois complementos que podem ser instalados directamente no Thunderbird:
* Chichi desenvolvido por Yannick: este módulo é recomendado porque oferece muitas outras características de acessibilidade e o ThunderbirdPlus foi concebido para interagir com ele;
* Comece pela caixa de entrada : se não usar Chichi, este módulo faz um bom trabalho;

<a name=\"chichi\">

### Com Chichi 

Para utilizar Chichi, leia a secção de Download e Instalação e a secção Set Startup Folder da [página Chichi](https://www.rptools.org//Outils-DV/thunderbird-chichi-pt.html);

<a name=\"stwi\">

#### Com a caixa de entrada iniciar na caixa de entrada 
A partir de Outubro de 2022, a última versão deste módulo para o Thunderbird 102 era a 2.5.2.
Características :
* Instalação: através de uma pesquisa pelo nome no separador \"extras\" do Thunderbird;
* Pasta de arranque: sempre a mesma, a pasta de entrada de correio da conta escolhida nas configurações do módulo ou a pasta unificada ;
* Auto-focus: na última mensagem da lista de mensagens ou na pasta \"Incoming mail\" na árvore, dependendo da configuração nas opções do módulo. Esta segunda opção é seleccionada por defeito;
* Definições: acesso menos fácil. Tem de ir ao separador extras, seleccionar \"iniciar na caixa de entrada\" na lista de extensões instaladas e depois premir enter no botão \"opções do módulo\", que abre um novo separador \"Settings Start with inbox\",
<br>Uma lista pendente permite-lhe escolher a conta de correio electrónico para a qual a pasta de correio recebido será seleccionada quando o Thunderbird iniciar,
<br>Três botões de rádio permitir-lhe-ão escolher o foco entre a última mensagem ou a primeira mensagem não lida na lista de mensagens ou a pasta na árvore;
<a name=\"stwInstall\">
Instalação:
* em Thunderbird, abra o menu \"Ferramentas\" e clique em : Módulos e temas adicionais ;
* Na página gestor de módulo, vá para o campo de pesquisa. No modo de navegação, pode premir a letra e para a alcançar rapidamente;
* escrever : Comece pela Caixa de Entrada e prima Enter ;
* Se tiver Thunderbird+4, aguarde um momento até seleccionar o módulo que procura no separador de resultados;
* Em alternativa, seleccione manualmente o separador \"iniciar com caixa de entrada:: Search :: Modules for Thunderbird\", por exemplo. Depois prima a tecla 3 ou citação até alcançar o título de nível 3 com o nome do módulo que pesquisou;
* Usando a seta para baixo, desça até ao link \"adicionar ao thunderbird\" e carregue em Enter;
* Seguir o procedimento e reiniciar o Thunderbird;
* Se tudo correr bem, o Thunderbird abrirá no separador principal e dará foco à lista de mensagens;
Definir as opções Iniciar com a Caixa de Entrada :
* Voltar para o separador \"Gestor de extras\";
* Se necessário, deixar o campo de pesquisa para entrar no modo de navegação;
* Prima 3 tantas vezes quantas forem necessárias para atingir o nível 3, \"iniciar com caixa de entrada\", na lista de módulos instalados;
* Depois clicar no botão: Opções do módulo. Isto abre um novo separador intitulado: configurações do início na caixa de entrada;
* Isto é o que é mostrado por defeito:
<Translators: para inglês, colocar a secção \"Interpretation into French\" como comentário para mostrar aos outros tradutores o que devem fazer -->
Em inglês :
Iniciar com a Caixa de Entrada - Configurações 
Por favor seleccione a conta, para a qual a caixa de entrada será mostrada após o início do Thunderbird. 
lista pendente: \\<A sua primeira conta de e-mail
Seleccionar e activar o foco:
botão de rádio clicável não verificado: a última* mensagem. 
botão de rádio desmarcado que pode clicar na pasta da caixa de entrada na árvore de pastas. 
Vazio
botão de rádio verificado: a primeira mensagem não lida. 
* Definição de \"último\": A última mensagem que foi colocada na caixa de entrada (independente da data
da mensagem).
Se a caixa de entrada não contiver mensagens, a pasta da caixa de entrada na árvore de pastas será seleccionada e 
sob o bloco.
Interpretação em francês : 
Comece com Inbox - Configurações ;
Seleccionar a conta cuja pasta de correio de entrada será mostrada quando o Thunderbird iniciar; 
Seleccionar emover o foco para
botão de rádio clicável sem marcação: A última mensagem da lista;
botão de rádio desmarcado clicável A pasta de entrada de correio na árvore de pastas ;
botão de rádio verificado: A primeira mensagem não lida na lista;
Se não houver mensagens na pasta a receber, esta pasta receberá o foco na árvore de pastas; 
Uma vez feitas as configurações, reinicie Thunderbird.
Thunderbird's lançador incorporado com AltGr+[Barra invertida](keyEquiv_pt_PT.html#aboveTab) :
Para comodidade e velocidade, pode lançar Thunderbird premindo AltGr+[Barra invertida](keyEquiv_pt_PT.html#aboveTab). 
Este atalho é configurável através do \"definir comandos\" d NVDA, que oferece mais liberdade de escolha de teclas modificadoras do que os atalhos do Windows, que estão limitados ao AltGr ;
Proceder como se segue para adicionar outro comando:
* Primeiro, trazer a janela Thunderbird para o primeiro plano;
* No submenu, prima Enter em : definir comandos\" ;
* No diálogo, prima a letra t até ouvir: \"Thunderbird, Launcher\";
* Desça até ao item: \"carregar o Thunderbird\" e prima a seta para a direita para expandir este nível;
* O lançador Thunderbird destina-se apenas à versão instalada do Thunderbird cujos caminhos Thunderbird.exe são previsíveis. 
* Numa configuração Windows de 64 bits, a extensão não lançará a versão de 32 bits do Thunderbird se ambas as versões de 64 bits e 32 bits estiverem instaladas no seu sistema; 

<!-- secção de links -->
[1]: https://www.nvaccess.org/addonStore/legacy?file=thunderbirdPlus

[2]: https://github.com/RPTools-org/ThunderbirdPlus/
