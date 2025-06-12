from manim import *
import random

class MontyHallSimulation(Scene):
    def construct(self):

        # Title first
        title = Tex("The Monty Hall Problem", color=WHITE).scale(1.2)
        self.play(Write(title))
        self.wait(2)

        # Shift title up
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # Create 3 doors horizontally
        door_positions = [-4, 0, 4]
        doors = VGroup()

        for pos in door_positions:
            door = Rectangle(height=4, width=2, color=WHITE, fill_color=BLUE_C, fill_opacity=1).scale(0.8)  # brown closed door
            door.move_to(RIGHT * pos)
            doors.add(door)  

        # Create circular number labels at center of each door
        number_labels = VGroup()

        for i, door in enumerate(doors):
            circle = Circle(radius=0.3, color=WHITE, fill_color=WHITE, fill_opacity=1)
            num = Text(str(i+1), color=BLACK, font_size=32)
            circle.move_to(door.get_center())
            num.move_to(circle.get_center())
            group = VGroup(circle, num)
            number_labels.add(group)

        # Animate doors and labels appearing
        self.play(Create(doors), FadeIn(number_labels))
        self.wait(1)

        # Randomly assign Car and Goats
        items = ["Car", "Goat", "Goat"]
        random.shuffle(items)

        # Store the door contents for later
        self.door_contents = items
        self.doors = doors
        self.number_labels = number_labels

        self.wait(2)

        # Debug print (optional)
        for i, content in enumerate(items):
            print(f"Door {i+1}: {content}")

        self.indicate_door(0)
        self.wait()

        self.open_door(2)
        self.wait(1)

        self.show_stay_switch_labels(0,1)
        self.wait()

        arrows = VGroup()
        for door in self.doors:
            arrow = Arrow(start=door.get_top() + UP * 0.5, end=door.get_top() + 0.1*UP, color=WHITE, stroke_width=5)
            arrows.add(arrow)
        
        self.show_prob_labels(0,1, arrows)
        self.wait()


    # Function to open door by fading it
    def open_door(self, door_index):
        door = self.doors[door_index]
        self.play(door.animate.set_fill(opacity=0.2))
        self.wait(0.5)
    
    # Function to indicate picked door
    def indicate_door(self, door_index):
        door = self.doors[door_index]
        label = self.number_labels[door_index]

        indication = Indicate(door, color=BLUE, scale_factor=1.1)
        label_flash = Indicate(label, color=BLUE, scale_factor=1.1)

        self.play(indication, label_flash)
        self.wait(0.5)

    def show_stay_switch_labels(self, stay_index, switch_index):
        stay_label = Tex("Stay", font_size=36, color=GREEN).next_to(self.doors[stay_index], DOWN, buff=0.5)
        switch_label = Tex("Switch", font_size=36, color=YELLOW).next_to(self.doors[switch_index], DOWN, buff=0.5)

        self.play(FadeIn(stay_label), FadeIn(switch_label))
        self.wait(1)

        # Store them if you want to remove later
        self.stay_label = stay_label
        self.switch_label = switch_label
    
    def show_prob_labels(self, stay_index, switch_index, arrows):
        # Main labels: Stay and Switch
        stay_label = Tex("Stay", font_size=36, color=GREEN).next_to(self.doors[stay_index], DOWN, buff=0.5)
        switch_label = Tex("Switch", font_size=36, color=YELLOW).next_to(self.doors[switch_index], DOWN, buff=0.5)

        # Probability labels
        stay_prob = Tex(r"$P(\text{stay}) = \frac{1}{3} \approx 33\%$", font_size=28, color=WHITE).next_to(stay_label, DOWN, buff=0.3)
        switch_prob = Tex(r"$P(\text{switch}) = \frac{2}{3} \approx 67\%$", font_size=28, color=WHITE).next_to(switch_label, DOWN, buff=0.3)

        # Animate appearance
        self.play(FadeIn(stay_prob))
        self.show_arrow(0, arrows)
        self.play(FadeIn(switch_prob), Transform(arrows[0].copy(), arrows[1]))
        self.wait(1)

    def show_arrow(self, door_index, arrows):
        arrow = arrows[door_index]
        self.play(FadeIn(arrow))
        self.wait(0.5)


import math

class MontyHallGeneralized(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"

        N = 40 # You can change this to 10, 20, 50, 100...

        # Create doors
        doors = self.create_doors_grid(N)
        self.play(LaggedStart(*[FadeIn(door) for door in doors], lag_ratio=0.02))
        self.wait(1)

    def create_doors_grid(self, N):
        doors = VGroup()

        # Arrange in grid
        n_cols = min(N, 10)  # max 10 columns, rest will wrap to new row
        n_rows = math.ceil(N / n_cols)

        for idx in range(N):
            row = idx // n_cols
            col = idx % n_cols

            door = Rectangle(height=1, width=0.6, color=WHITE, fill_color=BLUE_C, fill_opacity=1)

            # Compute position
            x_offset = (col - (n_cols - 1) / 2) * 0.9
            y_offset = ((n_rows - 1) / 2 - row) * 1.4
            door.move_to(RIGHT * x_offset + UP * y_offset)

            # Add number circle inside door
            circle = Circle(radius=0.15, color=WHITE, fill_color=WHITE, fill_opacity=1)
            num = Text(str(idx+1), color=BLACK, font_size=18)
            circle.move_to(door.get_center())
            num.move_to(circle.get_center())

            group = VGroup(door, circle, num)
            doors.add(group)

        self.doors = doors  # store for later if needed
        return doors


class Classic3DoorVersion(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"

        # Title
        title = Tex(r"\textbf{Classic 3-Door Version}", color=WHITE).scale(1.2)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # Create 3 doors horizontally
        door_positions = [-4, 0, 4]
        doors = VGroup()
        number_labels = VGroup()

        for i, pos in enumerate(door_positions):
            door = Rectangle(height=4, width=2, color=WHITE, fill_color=BLUE_C, fill_opacity=1).scale(0.8)
            door.move_to(RIGHT * pos)
            doors.add(door)

            circle = Circle(radius=0.3, color=WHITE, fill_color=WHITE, fill_opacity=1)
            num = Text(str(i+1), color=BLACK, font_size=36)
            circle.move_to(door.get_center())
            num.move_to(circle.get_center())
            number_labels.add(VGroup(circle, num))

        self.play(Create(doors), FadeIn(number_labels))
        self.wait(1)

        # Probability labels
        prob_labels = VGroup(
            Tex(r"$\frac{1}{3}$", font_size=36, color=WHITE).next_to(doors[0], UP, buff=0.3),
            Tex(r"$\frac{1}{3}$", font_size=36, color=WHITE).next_to(doors[1], UP, buff=0.3),
            Tex(r"$\frac{1}{3}$", font_size=36, color=WHITE).next_to(doors[2], UP, buff=0.3),
        )

        self.play(FadeIn(prob_labels))
        self.wait(1)

        # Show combined 2/3 probability rectangle
        group_for_2over3 = VGroup(doors[1], doors[2])
        rect_2over3 = SurroundingRectangle(group_for_2over3, color=YELLOW, buff=0.3)
        label_2over3 = Tex(r"$\frac{2}{3}$", font_size=40, color=YELLOW).next_to(rect_2over3, UP, buff=0.2)

        self.play(Create(rect_2over3), FadeIn(label_2over3))
        self.wait(2)

        # Simulate Monty opening Door 3 (index 2)
        self.play(doors[2].animate.set_fill(opacity=0.2))
        self.wait(1)

        # Animate rectangle shrinking to Door 2 (index 1)
        rect_final = SurroundingRectangle(doors[1], color=YELLOW, buff=0.3)
        self.play(Transform(rect_2over3, rect_final), FadeOut(prob_labels[1:3]), label_2over3.animate.next_to(rect_final, UP, buff=0.2))
        self.wait(2)

        # Small pause to emphasize final result
        self.play(Indicate(doors[1], color=YELLOW))
        self.wait(2)

class GeneralizedMontyHallN(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"

        # Title
        title = Tex(r"\textbf{Generalized Version}", color=WHITE).scale(1.2)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        #### First 3 doors: 1, 2, 3 ####

        door_positions = [-4, -2.5, -1]
        doors_initial = VGroup()

        for idx, pos in enumerate(door_positions):
            door = Rectangle(height=3, width=1.5, color=WHITE, fill_color=BLUE_C, fill_opacity=1).scale(0.6)
            door.move_to(RIGHT * pos)

            circle = Circle(radius=0.3, color=WHITE, fill_color=WHITE, fill_opacity=1)
            num = Text(str(idx+1), color=BLACK, font_size=32)
            circle.move_to(door.get_center())
            num.move_to(circle.get_center())

            doors_initial.add(VGroup(door, circle, num))

        self.play(LaggedStart(*[FadeIn(door) for door in doors_initial], lag_ratio=0.3))
        self.wait(0.5)

        # First probability label above Door 1
        prob_first = Tex(r"$\frac{1}{N}$", font_size=36, color=WHITE).next_to(doors_initial[0][0], UP, buff=0.4)

        #### Show dots ####
        dots = Tex(r"$\cdots$", font_size=80, color=WHITE).move_to(RIGHT*0.5)
        self.play(FadeIn(dots))
        self.wait(0.5)

        #### Last 3 doors: N-2, N-1, N ####

        final_positions = [2, 3.5, 5]
        doors_final = VGroup()
        final_labels = ["N-2", "N-1", "N"]

        for label, pos in zip(final_labels, final_positions):
            door = Rectangle(height=3, width=1.5, color=WHITE, fill_color=BLUE_C, fill_opacity=1).scale(0.6)
            door.move_to(RIGHT * pos)

            circle = Circle(radius=0.3, color=WHITE, fill_color=WHITE, fill_opacity=1)
            num = Text(label, color=BLACK, font_size=26)
            circle.move_to(door.get_center())
            num.move_to(circle.get_center())

            doors_final.add(VGroup(door, circle, num))

        self.play(LaggedStart(*[FadeIn(door) for door in doors_final], lag_ratio=0.3))
        self.wait(0.5)

        #### Show remaining probability ####

        group_rest = VGroup(doors_initial[1:], doors_final)
        surround = SurroundingRectangle(group_rest, color=YELLOW, buff=0.4)
        prob_rest = Tex(r"$1 - \frac{1}{N}$", font_size=36, color=YELLOW).next_to(surround, UP, buff=0.3)

        self.play(FadeIn(prob_first))
        self.wait(2)
        self.play(Create(surround), FadeIn(prob_rest))
        self.wait(2)

        self.play(VGroup(doors_initial[2], doors_final).animate.set_fill(opacity=0.2))
        self.wait(1)

        #### Collapse rectangle to final door N ####
        final_door_rect = doors_initial[1]
        surround_final = SurroundingRectangle(final_door_rect, color=YELLOW, buff=0.4)
        self.play(Transform(surround, surround_final), prob_rest.animate.next_to(surround_final, UP, buff=0.3))
        self.wait(1)

        #### Emphasize final door ####
        self.play(Indicate(final_door_rect, color=YELLOW))
        self.wait(2)

class GeneralizedMontyHall(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        N = 10  # You can set any N here

        # Title
        title = Tex(r"\textbf{Generalized Version}", color=WHITE).scale(1.2)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # Create doors in grid
        doors, door_rects = self.create_doors_grid(N)
        self.play(LaggedStart(*[FadeIn(door) for door in doors], lag_ratio=0.03))
        self.wait(1)

        # Assume player picks first door (index 0)
        player_pick = 0
        self.highlight_pick(player_pick, door_rects)

        # Show 1/N probability above chosen door
        prob_pick = Tex(rf"$\frac{{1}}{{{N}}}$", font_size=32, color=WHITE).next_to(door_rects[player_pick], UP, buff=0.2)
        self.play(FadeIn(prob_pick))

        # Group remaining doors for (N-1)/N probability
        other_doors = [door_rects[i] for i in range(N) if i != player_pick]
        group_other = VGroup(*other_doors)
        rect_group = SurroundingRectangle(group_other, color=YELLOW, buff=0.2)
        prob_other = Tex(rf"$\frac{{{N-1}}}{{{N}}}$", font_size=32, color=YELLOW).next_to(rect_group, UP, buff=0.2)
        self.play(Create(rect_group), FadeIn(prob_other))
        self.wait(1)

        # Simulate Monty opening all but one remaining goat doors
        unopened_index = 1  # Assume one remaining door is index 1 (can be randomized)
        to_open = [i for i in range(N) if i != player_pick and i != unopened_index]

        for i in to_open:
            self.play(door_rects[i].animate.set_fill(opacity=0.2), run_time=0.3)

        self.wait(1)

        # Animate rectangle collapsing onto remaining unopened door
        rect_final = SurroundingRectangle(door_rects[unopened_index], color=YELLOW, buff=0.2)
        self.play(Transform(rect_group, rect_final), prob_other.animate.next_to(rect_final, UP, buff=0.2))
        self.wait(1)

        # Emphasize final choice
        self.play(Indicate(door_rects[unopened_index], color=YELLOW))
        self.wait(2)

    def create_doors_grid(self, N):
        doors = VGroup()
        door_rects = []

        n_cols = min(N, 10)
        n_rows = math.ceil(N / n_cols)

        for idx in range(N):
            row = idx // n_cols
            col = idx % n_cols

            door = Rectangle(height=1, width=0.6, color=WHITE, fill_color=BLUE_C, fill_opacity=1).scale(1.5)

            x_offset = (col - (n_cols - 1) / 2)*1.2
            y_offset = ((n_rows - 1) / 2 - row) * 1.4
            door.move_to(RIGHT * x_offset + UP * y_offset)

            circle = Circle(radius=0.15, color=WHITE, fill_color=WHITE, fill_opacity=1)
            num = Text(str(idx+1), color=BLACK, font_size=18)
            circle.move_to(door.get_center())
            num.move_to(circle.get_center())

            label_group = VGroup(circle, num)
            doors.add(VGroup(door, label_group))
            door_rects.append(door)

        return doors, door_rects

    def highlight_pick(self, pick_idx, door_rects):
        door = door_rects[pick_idx]
        self.play(door.animate.set_color(YELLOW))
        self.wait(0.5)