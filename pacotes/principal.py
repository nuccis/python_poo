#import sound #Dessa maneira eu importo o pacote sound, mas não importo os seu subpacotes e nem submódulos

#from sound import* #Dessa maneira eu importo tudo o que estiver definido dentro da variavel __all__ no arquivo init do pacote sound. Isso vale também para os submódulos e subpacotes

#import sound.effects #Dessa maneira eu importo o pacote sound.effects, porém não importo os seus submódulos

'''import sound.effects.echo # posso importar diretamente o módulo desejado
sound.effects.echo.echoeffect()'''

'''import sound.effects.echo as seecho # posso importar diretamente o módulo desejado e mudar o nome da referencia à ele
seecho.echoeffect()'''

'''from sound.filters.karaoke import karaokefilter #posso importar diretamente uma função específica dentro de um módulo, porém não é muito indicado
karaokefilter()'''