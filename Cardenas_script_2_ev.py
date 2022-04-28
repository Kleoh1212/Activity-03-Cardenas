class pokeev():
    def statReturnDsi(base,iv,ev,Level):
        return((2*base+iv+(ev/4))*(Level/100))
  
    def statReturnEvs(stats,nature,dsi,Level):
        return(((((stats/nature)-dsi)*400)/Level)/4)*4