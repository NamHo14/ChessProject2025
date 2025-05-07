import pygame

#import Convert


class InitialBoard:
    def __init__(self,dimension,screen):
        self.dimension = dimension
        self.screen = screen

    #Function to SquareNumber to x,y
    def ConvertNumberToDimension(self,SquareNumber,dimension):
        x = (SquareNumber%8) * dimension/8
        y = (7-SquareNumber//8) * dimension/8
        return x,y

    #Function to draw the board squares
    def DrawBoard(self, screen,dimension):
        for square in range(64):
            X,Y = (self.ConvertNumberToDimension(square, dimension))
            if (square % 8) % 2 != (square // 8) % 2:
                pygame.draw.rect(screen, (227, 193, 111), [X, Y, self.dimension/8, self.dimension/8])
            else:
                pygame.draw.rect(screen, (184,139,74), [X, Y, self.dimension/8, self.dimension/8])

    #Function that check if the king castle to move the rook to the appropriate position
    def CastleRook(self, BoardPosition, MoveLog):
        if MoveLog:
            LastMove = MoveLog[-1]
            if LastMove[2] == "K" and LastMove[0:2] == "04" and LastMove[3:5] == "02":
                BoardPosition = BoardPosition[:3] + "R" + BoardPosition[4:]
                BoardPosition = BoardPosition[:0] + "0" + BoardPosition[1:]

            if LastMove[2] == "K" and LastMove[0:2] == "04" and LastMove[3:5] == "06":
                BoardPosition = BoardPosition[:5] + "R" + BoardPosition[6:]
                BoardPosition = BoardPosition[:7] + "0" + BoardPosition[8:]

            if LastMove[2] == "k" and LastMove[0:2] == "60" and LastMove[3:5] == "58":
                BoardPosition = BoardPosition[:59] + "r" + BoardPosition[60:]
                BoardPosition = BoardPosition[:56] + "0" + BoardPosition[57:]

            if LastMove[2] == "k" and LastMove[0:2] == "60" and LastMove[3:5] == "62":
                BoardPosition = BoardPosition[:61] + "r" + BoardPosition[62:]
                BoardPosition = BoardPosition[:63] + "0" + BoardPosition[64:]
        return BoardPosition

    # Function that checks if a pawn performed an en passant move an eliminated the appropriate move
    def EnPassantKill(self, BoardPosition, MoveLog):
        if len(MoveLog) > 1:
            LastMove = MoveLog[-1]
            BeforeLastMove = MoveLog[-2]

            if (int(BeforeLastMove[0:2]) - int(BeforeLastMove[3:5]) == 16) and (BeforeLastMove[2] == "p"):
                if (((abs(int(BeforeLastMove[3:5]) - int(LastMove[0:2]))) == 1) and (LastMove[2] == "P") and ((int(LastMove[3:5]) - int(LastMove[0:2]) == 9) or (int(LastMove[3:5]) - int(LastMove[0:2] == 7)))):
                    BoardPosition = BoardPosition[:int(BeforeLastMove[3:5])] + "0" + BoardPosition[int(BeforeLastMove[3:5])+1:]

            if (int(BeforeLastMove[0:2]) - int(BeforeLastMove[3:5]) == -16) and (BeforeLastMove[2] == "P"):
                if (((abs(int(BeforeLastMove[3:5]) - int(LastMove[0:2]))) == 1) and (LastMove[2] == "p") and (
                        (int(LastMove[3:5]) - int(LastMove[0:2]) == -9) or (int(LastMove[3:5]) - int(LastMove[0:2]) == -7))):
                    BoardPosition = BoardPosition[:int(BeforeLastMove[3:5])] + "0" + BoardPosition[int(BeforeLastMove[3:5]) + 1:]
        return BoardPosition

    #Function that draws the promotion choice
    def DrawPromotion(self, BoardPosition, screen):
        if "p" in BoardPosition[0:8]:
            index = BoardPosition[0:8].index("p")
            pygame.draw.rect(screen, (242, 242, 199), [(self.ConvertNumberToDimension(index, self.dimension))[0], self.ConvertNumberToDimension(index+24, self.dimension)[1], self.dimension / 8, self.dimension / 2])

            image_Queen = pygame.transform.scale(pygame.image.load("Chess_qdt60.png").convert_alpha(), (self.dimension / 8, self.dimension / 8))
            image_Rook = pygame.transform.scale(pygame.image.load("Chess_rdt60.png").convert_alpha(), (self.dimension / 8, self.dimension / 8))
            image_Bishop = pygame.transform.scale(pygame.image.load("Chess_bdt60.png").convert_alpha(), (self.dimension / 8, self.dimension / 8))
            image_Horse = pygame.transform.scale(pygame.image.load("Chess_ndt60.png").convert_alpha(),(self.dimension / 8, self.dimension / 8))
            screen.blit(image_Queen, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index, self.dimension)[1])))
            screen.blit(image_Rook, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index + 8, self.dimension)[1])))
            screen.blit(image_Bishop, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index + 16, self.dimension)[1])))
            screen.blit(image_Horse, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index + 24, self.dimension)[1])))

        elif "P" in BoardPosition[56:64]:
            index = BoardPosition[56:64].index("P")

            pygame.draw.rect(screen, (242, 242, 199), [((self.ConvertNumberToDimension(index+56, self.dimension))[0]),(self.ConvertNumberToDimension(index+56, self.dimension)[1]), self.dimension / 8, self.dimension / 2])

            image_Queen = pygame.transform.scale(pygame.image.load("Chess_qlt60.png").convert_alpha(), (self.dimension / 8, self.dimension / 8))
            image_Rook = pygame.transform.scale(pygame.image.load("Chess_rlt60.png").convert_alpha(), (self.dimension / 8, self.dimension / 8))
            image_Bishop = pygame.transform.scale(pygame.image.load("Chess_blt60.png").convert_alpha(), (self.dimension / 8, self.dimension / 8))
            image_Horse = pygame.transform.scale(pygame.image.load("Chess_nlt60.png").convert_alpha(),(self.dimension / 8, self.dimension / 8))

            screen.blit(image_Queen, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index+56, self.dimension)[1])))
            screen.blit(image_Rook, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index+48, self.dimension)[1])))
            screen.blit(image_Bishop, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index+40, self.dimension)[1])))
            screen.blit(image_Horse, ((self.ConvertNumberToDimension(index, self.dimension)[0]), (self.ConvertNumberToDimension(index+32, self.dimension)[1])))

    #function to determine if a Promotion piece was selected
    def PromotionSelect(self, MousePosition, MoveLog, BoardPosition,Turn):
        if MoveLog:
            LastMove = MoveLog[len(MoveLog)-1]
            PawnLocation = int(LastMove[3:5])

            if LastMove[2] == "P":
                if MousePosition == PawnLocation:
                    BoardPosition = BoardPosition[:PawnLocation] + "Q" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False, 1
                if MousePosition == (PawnLocation-8):
                    BoardPosition = BoardPosition[:PawnLocation] + "R" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False, 1
                if MousePosition == (PawnLocation-16):
                    BoardPosition = BoardPosition[:PawnLocation] + "B" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False,1
                if MousePosition == (PawnLocation-24):
                    BoardPosition = BoardPosition[:PawnLocation] + "H" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False,1

            if LastMove[2] == "p":
                if MousePosition == PawnLocation:
                    BoardPosition = BoardPosition[:PawnLocation] + "q" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False, 0
                if MousePosition == (PawnLocation+8):
                    BoardPosition = BoardPosition[:PawnLocation] + "r" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False, 0
                if MousePosition == (PawnLocation+16):
                    BoardPosition = BoardPosition[:PawnLocation] + "b" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False, 0
                if MousePosition == (PawnLocation+24):
                    BoardPosition = BoardPosition[:PawnLocation] + "h" + BoardPosition[PawnLocation+1:]
                    return BoardPosition, False, 0
        return BoardPosition, True, Turn

    #function to that determine if promotion is happening
    def Promotion(self, BoardPosition):
        if (("p" in BoardPosition[0:8]) or ("P" in BoardPosition[56:64])):
            return True
        return False

    #Function That the updates positionstring and movelog with new instruction
    def MovingPiece(self, PositionString, Instruction, MoveLog, update):
        if update==1:
            MoveLog.append(Instruction)
        if Instruction:
            InitialPosition = int(Instruction[0:2])
            PositionString = PositionString[:InitialPosition] + "0" + PositionString[InitialPosition + 1:]
            FinalPosition = int(Instruction[3:5])
            PositionString = PositionString[:FinalPosition] + Instruction[2] + PositionString[FinalPosition + 1:]
        PositionString = self.CastleRook(PositionString, MoveLog)
        PositionString = self.EnPassantKill(PositionString, MoveLog)
        return PositionString, MoveLog

    #Function that display endscreen
    def Endscreen(self,message,event):
        length = 7.75
        if message =="DRAW":
            length = 3

        rect = pygame.Rect(0, 0, (self.dimension/8)*length, (self.dimension/8)*1)
        rect.center = ((self.dimension/8)*4, (self.dimension/8)*3.5)
        pygame.draw.rect(self.screen, (217, 217, 145), rect)

        Messagerect = pygame.Rect(0, 0, (self.dimension / 8) * 4, (self.dimension / 8) * 0.75)
        Messagerect.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 4.5)
        pygame.draw.rect(self.screen, (217, 217, 145), Messagerect)

        Text_font = pygame.font.SysFont("Times New Roman", int(30*(self.dimension)/480),1)

        TextMessage = Text_font.render(message, True, (0,0,0))
        textRect = TextMessage.get_rect(center=((self.dimension/8)*4, (self.dimension/8)*3.5))

        self.screen.blit(TextMessage,textRect)

        RestartRect= Text_font.render("PLAY AGAIN", True, (0,0,0))
        restartRect = RestartRect.get_rect(center=((self.dimension/8)*4, (self.dimension/8)*4.5))
        self.screen.blit(RestartRect,restartRect)

        buttonRestart = pygame.Rect(0, 0, (self.dimension / 8) * 4, (self.dimension / 8) * 0.75)
        buttonRestart.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 4.5)

        if buttonRestart.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 255, 255), buttonRestart, 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonRestart.collidepoint(event.pos):
                return True
        return False

    #Function that display optionscreen
    def OptionScreen(self,event):
        Background = pygame.Rect(0, 0, (self.dimension / 8) * 5.5, (self.dimension / 8) * 3.5)
        Background.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 4.0)
        pygame.draw.rect(self.screen, (150, 163, 111), Background)

        Text_font = pygame.font.SysFont("Times New Roman", int(45*(self.dimension)/480))
        Menu = Text_font.render("MENU", True, (255, 255, 255))
        MenuRect = Menu.get_rect(center=((self.dimension / 8) * 4, (self.dimension / 8) * 2.75))
        self.screen.blit(Menu, MenuRect)

        Text_font = pygame.font.SysFont("Times New Roman", int(30*(self.dimension)/480))

        PlayerVsPlayertRect = Text_font.render("Player VS Player", True, (0, 0, 0))

        buttonPlayerVsPlayer = pygame.Rect(0, 0, (self.dimension / 8) * 4, (self.dimension / 8) * 1)
        buttonPlayerVsPlayer.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 3.75)
        pygame.draw.rect(self.screen, (217, 217, 145), buttonPlayerVsPlayer)

        PlayerRect = PlayerVsPlayertRect.get_rect(center=((self.dimension / 8) * 4, (self.dimension / 8) * 3.75))
        self.screen.blit(PlayerVsPlayertRect, PlayerRect)


        PlayerVSLevel1BotRect = Text_font.render("Player VS Batman", True, (0, 0, 0))

        buttonLevel1Bot = pygame.Rect(0, 0, (self.dimension / 8) * 4.0, (self.dimension / 8) * 1)
        buttonLevel1Bot.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 5.0)
        pygame.draw.rect(self.screen, (217, 217, 145), buttonLevel1Bot)

        PlayerVSLevel1Rect = PlayerVSLevel1BotRect.get_rect(center=((self.dimension / 8) * 4, (self.dimension / 8) * 5.0))
        self.screen.blit(PlayerVSLevel1BotRect, PlayerVSLevel1Rect)

        if buttonPlayerVsPlayer.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 255, 255), buttonPlayerVsPlayer, 3)

        if buttonLevel1Bot.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 255, 255),  buttonLevel1Bot, 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonPlayerVsPlayer.collidepoint(event.pos):
                return 1
            elif buttonLevel1Bot.collidepoint(event.pos):
                return 2
        return 0

    def settings(self,event):
        Background = pygame.Rect(0, 0, (self.dimension / 8) * 5.5, (self.dimension / 8) * 3.5)
        Background.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 4.0)
        pygame.draw.rect(self.screen, (150, 163, 111), Background)

        Text_font = pygame.font.SysFont("Times New Roman", int(45*(self.dimension)/480))
        Menu = Text_font.render("SETTING", True, (255, 255, 255))
        MenuRect = Menu.get_rect(center=((self.dimension / 8) * 4, (self.dimension / 8) * 2.75))
        self.screen.blit(Menu, MenuRect)

        buttonMenuScreen = pygame.Rect(0, 0, (self.dimension / 8) * 4, (self.dimension / 8) * 1)
        buttonMenuScreen.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 3.75)
        pygame.draw.rect(self.screen, (217, 217, 145), buttonMenuScreen)

        Text_font = pygame.font.SysFont("Times New Roman", int(30*(self.dimension)/480))

        MenuScreenText = Text_font.render("Menu", True, (0, 0, 0))

        MenuRect = MenuScreenText.get_rect(center=((self.dimension / 8) * 4, (self.dimension / 8) * 3.75))
        self.screen.blit(MenuScreenText, MenuRect)

        buttonReturnToGame = pygame.Rect(0, 0, (self.dimension / 8) * 4, (self.dimension / 8) * 1)
        buttonReturnToGame.center = ((self.dimension / 8) * 4, (self.dimension / 8) * 5.00)
        pygame.draw.rect(self.screen, (217, 217, 145), buttonReturnToGame)

        ReturnGameText = Text_font.render("Return To Game", True, (0, 0, 0))

        MenuRect = ReturnGameText.get_rect(center=((self.dimension / 8) * 4, (self.dimension / 8) * 5.00))
        self.screen.blit(ReturnGameText, MenuRect)

        if buttonMenuScreen.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 255, 255), buttonMenuScreen, 3)

        if buttonReturnToGame.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, (255, 255, 255),  buttonReturnToGame, 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonMenuScreen.collidepoint(event.pos):
                return 1
            elif buttonReturnToGame.collidepoint(event.pos):
                return 2
        return 0
        print("bob")

    def settingButton(self,event):
        image = pygame.image.load("PauseButton.png").convert_alpha()
        image = pygame.transform.scale(image, (self.dimension / 16, self.dimension / 16))
        self.screen.blit(image, (self.dimension-self.dimension / 16, 0))

        buttonSetting = pygame.Rect(self.dimension-self.dimension / 16, 0,self.dimension / 16,self.dimension / 16)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonSetting.collidepoint(event.pos):
                return True
        return False