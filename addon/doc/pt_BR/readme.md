# Thunderbird+

* Autor: Pierre-Louis Renaud (Thunderbird 78 a 102) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 68 a 91), Yannick (TB 45 a 60);
* URL: [Manual do utilizador][4] ;
  [História das mudanças em RPTools.org][5] ;
  [Contacto em inglês e francês][6];
* Descarregar a [versão estável][1]
* Descarregar a [Última versão em RPTools.org][3];
* Compatibilidade com o NVDA: 2019.3 e superior;
* Compatibilidade com o Thunderbird: versões 102.x;
* [Código fonte no gitHub][2]

## Descrição

Este extra melhora consideravelmente o conforto e a eficiência da utilização do cliente de correio electrónico Mozilla Thunderbird com NVDA.

As melhorias incluem os seguintes aspectos:

### Conforto auditivo

* Os alertas "tal pessoa solicitou um aviso de recepção" podem ser desactivados através de uma opção;
* Os avisos "Isto é um rascunho" e "o Thunderbird pensa que esta mensagem é fraudulenta" são simplesmente ignorados;
* Existem opções para desactivar o anúncio de nomes de listas de correio, para remover ou agrupar "RE" e para limpar os nomes dos correspondentes através da remoção de números e outros caracteres especiais irritantes;

### Navegação na janela principal

* A passagem para o painel seguinte é feita com a tecla TAB enquanto a tecla de escape é utilizada para regressar ao painel anterior. Isto é mais conveniente do que F6 e Shift+F6.
* A selecção de separadores com Control+Tab e Control+a número é vocalizada como neste exemplo: Separador 1 de 4, Correio recebido;
* Um atalho de teclado permite listar os separadores num menu para activar facilmente um deles;
* Um atalho de teclado é utilizado para mostrar o menu de contexto da barra de tabulação;

### Árvore de pastas

* Alt+ seta para baixo e Alt+ seta para cima para navegar entre pastas com mensagens não lidas;
* A digitação de uma letra ou número selecciona a pasta seguinte cujo nome começa com o carácter digitado. Ao premir a tecla Shift, o movimento é de baixo para cima. Além disso, é anunciado o nome da conta a que a pasta pertence;
* A tecla Espaço numa pasta com mensagens não lidas selecciona a primeira mensagem não lida na lista de mensagens;
* Dois diálogos das contas e as suas pastas associadas permitem filtrá-las por palavra-chave ou mostrar apenas as pastas com mensagens não lidas;

### Lista de mensagens

* A escolha das colunas e a sua disposição na lista de mensagens é acessibilizada através de um diálogo simples;
* Consulta das colunas da lista de mensagens: os atalhos permitem ouvir, soletrar ou copiar facilmente o nome do remetente, o assunto ou a data de uma mensagem, premindo um número no teclado alfanumérico: por exemplo, 1 ou & anuncia o remetente, 2 pressionamentos soletram o nome e 3 pressionamentos copiam-no para a área de transferência;
* Consulta dos cabeçalhos do painel de cabeçalhos apresentado com F8: com Alt+um número, 1 pressionamento indica um cabeçalho contendo os endereços do remetente ou dos destinatários, 2 pressionamentos abrem um diálogo que permite copiá-los, 3 pressionamentos abrem o menu contextual nativo de Thunderbird associado ao cabeçalho;
* Visualização rápida e limpa do texto da mensagem com espaço, Alt+ seta para baixo ou F4: os cabeçalhos de grandes blocos nas citações das mensagens são substituídos pela frase "O nome do remetente escreveu". A NVDA anunciará também "link clicável" em vez do endereço longo do link.
* Visão rápida das citações em ordem cronológica, de baixo para cima, usando Shift+Espaço, Alt+Up seta ou Shift+F4;
* Fácil acesso a anexos com o atalho Alt+ página seguinte ou com o número 1 no teclado alfanumérico;

### Barra de filtragem rápida e gestão de etiquetas prioritárias

* É possível navegar através das opções de filtro usando as setas verticais. A tecla Enter é utilizada para verificar ou desmarcar uma opção;
* As etiquetas são adicionadas ou removidas premindo Shift+um número no teclado alfanumérico. Por exemplo, premir 4 para adicionar a etiqueta "To Do" a uma mensagem. A lista de mensagens pode então ser filtrada por etiqueta através da barra de filtro rápido que está agora disponível;

### Janela para escrever uma mensagem

Alt+1 anuncia o Remetente, Alt+2 o Destinatário, Alt+3 os Anexos, etc. Dois pressionamentos colocam o foco num destes campos;

### Diálogo de verificação ortográfica

* A palavra mal escrita é anunciada com ou sem ortografia antes da palavra sugerida. Os atalhos NVDA+Tab ou seta Alt+up anunciam palavras mal escritas e substituídas: 1 pressionamento soletra as palavras à velocidade normal, 2 pressionamentos soletra-nas rapidamente, 3 pressionamentos copiam a palavra mal escrita para a área de transferência para análise num outro campo de edição;
* Várias combinações da tecla enter activam os botões Replace, Replace All, Ignore, Ignore All ou Add Word to Dictionary foram adicionados para maior comodidade a este diálogo;

### Actualização automática

O ThunderbirdPlus tem um sistema independente de actualização automática com opções de desactivação/activação e adiamento;

### Trabalhar em duo com Chichi

O ThunderbirdPlus foi concebido para funcionar em harmonia com Chichi, um add-on que é instalado directamente no Thunderbird.

Leia sobre isto na [página da Chichi][7];


E muitas outras coisas que descobrirá ao ler o [manual do utilizador][4] ;

<!-- Tradutores: nas hiperligações 4, 5 e 7 abaixo, onde aparece lang=en, substitua en pelo código da sua língua -->

[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.9.5/thunderbirdPlus-4.9.5-TB102.nvda-addon

[2]: https://github.com/RPTools-org/ThunderbirdPlus/

[3]: https://www.rptools.org/?p=8610

[4]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=manual&lang=pt_PT

[5]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=changes&lang=pt_PT

[6]: https://www.rptools.org/NVDA-Thunderbird/toContact.html

[7]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=chichi&lang=pt_PT
