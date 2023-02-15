from frame import Frame

class Player:

    def __init__(self,name):
        self.name = name
        self.total = 0
        self.scores = []
    
    def play(self, current_frame):
        # play one frame for the player
        frame = Frame(current_frame) #frame.next (strike/spare/none), frame.score (total), frame.first
        self.scores.append(frame)
        self.total += frame.score
        if current_frame != 1:
            if self.scores[current_frame-2].next == "strike":
                self.scores[current_frame-2].score += frame.score
                self.total += frame.score
            elif self.scores[current_frame-2].next == "spare":
                self.scores[current_frame-2].score += frame.first
                self.total += frame.first
        return self.scores
        
