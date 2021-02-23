"""Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  ####### """

for i in range(0,7):
    for j in range(0,7):
        if i>=j:
            print("#",end="")
    print()    
