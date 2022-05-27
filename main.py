import PIL
from geopy.distance import geodesic
from opencage.geocoder import OpenCageGeocode
from tkinter import *
from PIL import ImageTk
import tkinter as tk
from function import *
from tkinter import *
from supabase_class import *
from tkinter import messagebox
import tkinter as tk
from supabase import create_client, Client
#Api
supabase: Client = create_client("https://pxhugmeuqqfordqqnbus.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB4aHVnbWV1cXFmb3JkcXFuYnVzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTE1MDA5MDIsImV4cCI6MTk2NzA3NjkwMn0.3TneTInaPc2KaLE4Ujc3sri1FtSv_Hv_vLxeWYsPtPM")

# Connected User
user = User_Supabase("", "", "", "")


class RoundedButton(tk.Canvas):
    def __init__(self, parent, border_radius, padding, font_size, text_color, width, height, color, text='',
                 command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="raised", highlightthickness=0, bg=parent["bg"])
        self.command = command

        if border_radius > 0.5 * width:
            print("Error: border_radius is greater than width.")
            return None

        if border_radius > 0.5 * height:
            print("Error: border_radius is greater than height.")
            return None

        rad = 2 * border_radius

        def shape():
            self.create_arc((0, rad, rad, 0),
                            start=90, extent=90, fill=color, outline=color)
            self.create_arc((width - rad, 0, width,
                             rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width, height - rad, width - rad,
                             height), start=270, extent=90, fill=color, outline=color)
            self.create_arc((0, height - rad, rad, height), start=180, extent=90, fill=color, outline=color)
            return self.create_polygon(
                (0, height - border_radius, 0, border_radius, border_radius, 0, width - border_radius, 0, width,
                 border_radius, width, height - border_radius, width - border_radius, height, border_radius, height),
                fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")

        self.create_text(width / 2, height / 2, text=text, fill=text_color, font=(LARGEFONT, font_size))
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

class RoundedButton_V2(tk.Canvas):
    def __init__(self, parent, border_radius, padding, font_size, text_color, width, height, color, text='',
                 command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="raised", highlightthickness=0, bg=parent["bg"])
        self.command = command

        borderwidth = 0
        if border_radius > 0.5 * width:
            print("Error: border_radius is greater than width.")
            return None

        if border_radius > 0.5 * height:
            print("Error: border_radius is greater than height.")
            return None

        rad = 2 * border_radius

        def shape():
            self.create_arc((0, rad, rad, 0),
                            start=90, extent=90, fill=color, outline=color)
            self.create_arc((0, height - rad, rad, height), start=180, extent=90, fill=color, outline=color)
            return self.create_polygon(
                (0, height - border_radius, 0, border_radius, border_radius, 0, width, 0, width,
                 border_radius, width, height - border_radius, width, height, border_radius, height),
                fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")

        self.create_text(width / 2, height / 2, text=text, fill=text_color, font=(LARGEFONT, font_size))
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

class RoundedButton_V3(tk.Canvas):
    def __init__(self, parent, border_radius, padding, font_size, text_color, width, height, color, text='',
                 command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="raised", highlightthickness=0, bg=parent["bg"])
        self.command = command

        borderwidth = 0
        if border_radius > 0.5 * width:
            print("Error: border_radius is greater than width.")
            return None

        if border_radius > 0.5 * height:
            print("Error: border_radius is greater than height.")
            return None

        rad = 2 * border_radius

        def shape():
            self.create_arc((0, rad, rad, 0),
                            start=90, extent=90, fill=color, outline=color)
            self.create_arc((width - rad, 0, width,
                             rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width, height - rad, width - rad,
                             height), start=270, extent=90, fill=color, outline=color)
            self.create_arc((0, height - rad, rad, height), start=180, extent=90, fill=color, outline=color)
            return self.create_polygon(
                (0, height - border_radius, 0, 0, border_radius, 0, width - border_radius, 0, width,
                 border_radius, width, height - border_radius, width - border_radius, height, 0, height),
                fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")

        self.create_text(width / 2, height / 2, text=text, fill=text_color, font=(LARGEFONT, font_size))
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

def Navbar(self, controller, active="HOME"):
    self.configure(bg='#333333')
    
    btnHome = Button(self, text="Home", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "HOME" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                     command=lambda: [controller.frames[Home].update(controller), controller.show_frame(Home)])
    btnHome.place(x=180, y=15)

    btnPost = Button(self, text="My posts", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "POST" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                     command=lambda: [controller.frames[Post].update(controller), controller.show_frame(Post)])
    btnPost.place(x=260, y=15)

    btnPlanning = Button(self, text="Planning", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "PLANNING" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                    command=lambda: [controller.frames[Planning].update(controller), controller.show_frame(Planning)])
    btnPlanning.place(x=340, y=15)

    btnFind = Button(self, text="FindTravel", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "FINDTRAVEL" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                     command=lambda: controller.show_frame(FindTravel))
    btnFind.place(x=420, y=15)

    btnHistory = Button(self, text="History", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "HISTORY" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                     command=lambda: controller.show_frame(History))
    btnHistory.place(x=500, y=15)

    btnMess = Button(self, text="Message", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "MESSAGE" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                     command=lambda: [controller.frames[Message].update(controller), controller.show_frame(Message)])
    btnMess.place(x=780, y=15)

    btnProfile = Button(self, text="Profile", bg='#333333', borderwidth=0,
                     fg="#6B6B6B" if active == "PROFILE" else '#E2E3D9', activebackground='#333333',
                     activeforeground='#6B6B6B',
                     command=lambda: [controller.frames[Profile].update(controller), controller.show_frame(Profile)])
    btnProfile.place(x=860, y=15)

    logo = PIL.Image.open("Fichier 2.png")
    logo = logo.resize((40, 50))
    photoLogo = ImageTk.PhotoImage(logo)
    labelLogo = tk.Label(self, image=photoLogo, borderwidth=0, relief="flat")
    labelLogo.image = photoLogo
    labelLogo.place(x=100, y=0)

def resetWindowInfo(self):
    for child in self.winfo_children():
        if (child['bg'] == '#303030'):
            child.destroy()

def travelInfo(self, info, controller):
    if self.open == False:
        frame1 = tk.Frame(self, width=500, height=718, background="#303030")
        frame1.place(x=524, y=50)
        button2 = RoundedButton(frame1, text="X", width=30, border_radius=8, padding=4, font_size=10,
                                text_color="#4E4E4E", color="#E2E3D9", height=30,
                                command=lambda: resetWindowInfo(self))
        button2.place(x=430, y=30)
        label0 = Label(frame1, text=info['fullname'] + " " + info["start_date"], font=14, bg="#303030", fg="white")
        label0.place(x=50, y=110)
        label = Label(frame1, text=info['dest_from'] + "   ➡    " + info["dest_to"], font=11, bg="#303030", fg="white")
        label.place(x=50, y=160)
        label1 = Label(frame1, text=str(info["distance"]) + "Km", font=(LARGEFONT, 12), bg="#303030", fg="white")
        label1.place(x=50, y=190)
        label2 = Label(frame1, text=str(info["price"]) + " €", font=(LARGEFONT, 11), bg="#303030", fg="white")
        label2.place(x=50, y=210)
        button2 = RoundedButton(frame1, text="Annuler le voyage?", width=200, border_radius=8, padding=4, font_size=10,
                                text_color="#4E4E4E", color="#E2E3D9", height=30,
                                command=lambda: cancelTravel(info["id"]))
        button2.place(x=250, y=320)

def cancelTravel(uuid):
    data = supabase.table("travel").delete().eq("id", uuid).execute()

def clear_entry(event, entry):
    entry.delete(0, END)
    entry.unbind('<Button-1>', "")

LARGEFONT = ("Verdana", 35)

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, Post, Planning, FindTravel, History, Message, Profile, Login, Register):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(Login)
    # to display the current frame passed as
    # parameter

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "HOME")
        self.bodyHome(controller)

    def update(self, controller):
        self.bodyHome(controller)


    def bodyHome(self, controller):
        frame1 = tk.Frame(self, width=1024, height=568, background="#4E4E4E")
        frame1.place(x=0, y=50)

        data = supabase.rpc("get_next_travel", {"search_id": str(user.id)}).execute().data
        if(len(data)!=0):
            print(data[0])
            button2 = RoundedButton(frame1, text="", width=800, border_radius=8, padding=4, font_size=10,
                                    text_color="#4E4E4E", color="#E2E3D9", height=100,
                                    command=lambda: [])
            button2.place(x=100, y=40 )
            label = Label(self, text=data[0]['dest_from'] + "   ➡    " + data[0]["dest_to"], font=10, bg="#E2E3D9")
            label.place(x=110, y=100)
            label1 = Label(self, text=str(data[0]["distance"]) + " km " + data[0]["start_date"],
                        font=(LARGEFONT, 10), bg="#E2E3D9")
            label1.place(x=110, y=130)
            label2 = Label(self, text=data[0]["fullname"] + " " + str(data[0]["age_user"]), font=(LARGEFONT, 10),
                        bg="#E2E3D9")
            label2.place(x=110, y=160)
        
            button2 = RoundedButton(frame1, text="Search Travel\n         🔎", width=390, font_size=20, border_radius=8,
                                    padding=4, text_color="#4E4E4E", color="#E2E3D9",
                                    height=220, command=lambda: controller.show_frame(FindTravel))
            button2.place(x=100, y=200)

            button3 = RoundedButton(frame1, text="Create a post\n         ➕", border_radius=8, padding=4, text_color="#4E4E4E",
                                    color="#E2E3D9", width=390, font_size=20,
                                    height=220, command=lambda: controller.show_frame(FindTravel))
            button3.place(x=510, y=200)
        else:
            button1 = RoundedButton(frame1, text="My posts \n     😀", width=800, font_size=20, border_radius=8, padding=4,
                                    text_color="#4E4E4E", color="#E2E3D9",
                                    height=220, command=lambda: controller.show_frame(Post))
            button1.place(x=100, y=40)
            button2 = RoundedButton(frame1, text="Search Travel\n         🔎", width=390, font_size=20, border_radius=8,
                                    padding=4, text_color="#4E4E4E", color="#E2E3D9",
                                    height=220, command=lambda: controller.show_frame(FindTravel))
            button2.place(x=100, y=275)

            button3 = RoundedButton(frame1, text="Create a post\n         ➕", border_radius=8, padding=4, text_color="#4E4E4E",
                                    color="#E2E3D9", width=390, font_size=20,
                                    height=220, command=lambda: controller.show_frame(FindTravel))
            button3.place(x=510, y=275)


class Post(tk.Frame):

    def find_distance(self, A, B):
        key = 'dabcd57e3a714a138b617b172ed7f3c2'
        geocoder = OpenCageGeocode(key)

        result_A = geocoder.geocode(A)
        lat_A = result_A[0]['geometry']['lat']
        lng_A = result_A[0]['geometry']['lng']

        result_B = geocoder.geocode(B)
        lat_B = result_B[0]['geometry']['lat']
        lng_B = result_B[0]['geometry']['lng']

        return str(round(geodesic((lat_A, lng_A), (lat_B, lng_B)).kilometers))

    def definePrice(self, distance):
        return ((distance*5)/100)*1.9

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "POST")
        self.bodyPost(controller)

    def bodyPost(self, controller):
        frame1 = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        frame1.place(x=0, y=50) 

        title_label = Label(self, text="My Posts", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
        title_label.place(x=100, y=80)
        add_btn = RoundedButton(frame1, text="➕", border_radius=8, padding=4, text_color="#ED7B32",color="#FFFFFF", width=28, font_size=15,height=28, command=lambda: self.createPost(controller))
        add_btn.place(x=870, y=30)

        data = supabase.rpc("get_my_posts", {"search_id": str(user.id)}).execute().data
        if(len(data) == 0):
            title_label = Label(self, text="You don't have any post", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
            title_label.place(x=400, y=300)
        else:
            for i in range(len(data)):
                button2 = RoundedButton(frame1, text="", width=800, border_radius=8, padding=4, font_size=10,
                                        text_color="#4E4E4E", color="#E2E3D9", height=100,
                                        command=lambda: [])
                button2.place(x=100, y=100 + (i * 120))
                label = Label(self, text=data[i]['dest_from'] + "   ➡    " + data[i]["dest_to"], font=10, bg="#E2E3D9")
                label.place(x=110, y=160 + (i * 120))
                label1 = Label(self, text=str(data[i]["distance"]) + " km " + data[i]["start_date"],
                            font=(LARGEFONT, 10), bg="#E2E3D9")
                label1.place(x=110, y=190 + (i * 120))
                label2 = Label(self, text=data[i]["fullname"] + " " + str(data[i]["age_user"]), font=(LARGEFONT, 10),
                            bg="#E2E3D9")
                label2.place(x=110, y=210 + (i * 120))
                label4 = Label(self, text=str(data[i]["price"]) + " €", font=(LARGEFONT, 10), bg="#E2E3D9")
                label4.place(x=830, y=160 + (i * 120))
                label4 = Label(self, text=str(data[i]["left_seat"]) + " seats left", font=(LARGEFONT, 10), bg="#E2E3D9")
                label4.place(x=830, y=180 + (i * 120))

                del_btn = RoundedButton(frame1, text="🗑", border_radius=0, padding=0, text_color="#ED7B32",color="#E2E3D9", width=35, font_size=22,height=35, command=lambda i=i: self.deletePost(data[i]['travel_id'], controller))
                del_btn.place(x=850, y=155 + (i * 120))

    def deletePost(self, id, controller):
        try:
            supabase.rpc("delete_travel", {"travel_id": str(id)}).execute()
        except:
            self.bodyPost(controller)

    def update(self, controller):
        self.bodyPost(controller)

    def createPost(self, controller):
        frame1 = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        frame1.place(x=0, y=50) 

        title_label = Label(self, text="Create a Travel", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
        title_label.place(x=100, y=80)

        from_input = tk.Entry(frame1,width=35)
        from_input.place(x=180, y=100, height=50)

        button= RoundedButton_V2(frame1, text="From", width=80, border_radius=8, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#ED7B32", height=50,
                                command=lambda: [])
        button.place(x=100, y=100)

        from_btn = RoundedButton_V3(frame1, text="", width=30, border_radius=12, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#FFFFFF", height=50,
                                command=lambda: [])
        from_btn.place(x=380, y=100)

        label = Label(self, text="➡", font=80, fg="#E2E3D9", bg="#4E4E4E")
        label.place(x=500, y=160)

        to_input = tk.Entry(frame1,width=35)
        to_input.place(x=680, y=100, height=50)

        button1 = RoundedButton_V2(frame1, text="To", width=80, border_radius=8, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#ED7B32", height=50,
                                command=lambda: [])
        button1.place(x=600, y=100)
        to_btn = RoundedButton_V3(frame1, text="", width=30, border_radius=12, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#FFFFFF", height=50,
                                command=lambda: [])
        to_btn.place(x=880, y=100)

        date_label = Label(self, text="Date", font=(LARGEFONT, 12), fg="#333333", bg="#4E4E4E")
        date_label.place(x=100, y=220)
        year_input = tk.Entry(frame1,width=10)
        year_input.insert(END, '2022')
        year_input.place(x=100, y=200, height=30)
        month_input = tk.Entry(frame1,width=10)
        month_input.insert(END, '05')
        month_input.place(x=170, y=200, height=30)
        day_input = tk.Entry(frame1,width=10)
        day_input.insert(END, '27')
        day_input.place(x=240, y=200, height=30)

        time_label = Label(self, text="Time", font=(LARGEFONT, 12), fg="#333333", bg="#4E4E4E")
        time_label.place(x=350, y=220)
        hour_input = tk.Entry(frame1,width=10)
        hour_input.insert(END, '18')
        hour_input.place(x=350, y=200, height=30)
        min_input = tk.Entry(frame1,width=10)
        min_input.insert(END, '30')
        min_input.place(x=420, y=200, height=30)

        info_label = Label(self, text="Informations", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
        info_label.place(x=100, y=340)

        seat_input = tk.Entry(frame1,width=35)
        seat_input.place(x=180, y=330, height=50)

        button= RoundedButton_V2(frame1, text="Seat", width=80, border_radius=8, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#ED7B32", height=50,
                                command=lambda: [])
        button.place(x=100, y=330)

        from_btn = RoundedButton_V3(frame1, text="", width=30, border_radius=12, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#FFFFFF", height=50,
                                command=lambda: [])
        from_btn.place(x=380, y=330)

        price_input = tk.Entry(frame1,width=35)
        price_input.place(x=680, y=330, height=50)

        button1 = RoundedButton_V2(frame1, text="Price", width=80, border_radius=8, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#ED7B32", height=50,
                                command=lambda: [])
        button1.place(x=600, y=330)
        to_btn = RoundedButton_V3(frame1, text="", width=30, border_radius=12, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#FFFFFF", height=50,
                                command=lambda: [])
        to_btn.place(x=880, y=330)


        create_button = RoundedButton(frame1, text="Create", width=360, border_radius=8, padding=4, font_size=15,
                                    text_color="#FFFFFF", color="#ED7B32", height=50,
                                    command=lambda: self.create(controller, {'from' : from_input.get(), "to": to_input.get(), "at": year_input.get()+"-"+month_input.get()+"-"+day_input.get()+ " "+hour_input.get()+":"+ min_input.get()+ ':00', "seat": seat_input.get(), "price": price_input.get()}))
        create_button.place(x=320, y=450)
       
    def create(self, controller, data):
        supabase.table("travel").insert({"total_seat":data['seat'], "left_seat":data['seat'], "created_by": str(user.id), "dest_from": data["from"], "dest_to": data['to'], "price": data['price'], "start_date": data['at'], "distance": self.find_distance(data["from"],data['to'])}).execute()
        self.bodyPost(controller)


class Planning(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "PLANNING")
        self.bodyPlanning(controller)

    def update(self, controller):
        self.bodyPlanning(controller)

    def bodyPlanning(self, controller):
        frame1 = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        frame1.place(x=0, y=50) 

        title_label = Label(self, text="Next Travel", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
        title_label.place(x=100, y=80)
        data = supabase.rpc("get_planning", {"search_id": str(user.id)}).execute().data

        if(len(data) == 0):
            title_label = Label(self, text="You don't have travel incomming", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
            title_label.place(x=350, y=300)
        else:
            self.componentTravel(controller=controller, frame=frame1, data=data)

    def componentTravel(self, controller, frame, data):
        for i in range(len(data)):
            button2 = RoundedButton(frame, text="", width=800, border_radius=8, padding=4, font_size=10,
                                    text_color="#4E4E4E", color="#E2E3D9", height=100,
                                    command=lambda i=i: travelInfo(self, data[i], controller))
            button2.place(x=100, y=100 + (i * 120))
            label = Label(self, text=data[i]['dest_from'] + "   ➡    " + data[i]["dest_to"], font=10, bg="#E2E3D9")
            label.place(x=110, y=160 + (i * 120))
            label1 = Label(self, text=str(data[i]["distance"]) + " km " + data[i]["start_date"],
                        font=(LARGEFONT, 10), bg="#E2E3D9")
            label1.place(x=110, y=190 + (i * 120))
            label2 = Label(self, text=data[i]["fullname"] + " " + str(data[i]["age_user"]), font=(LARGEFONT, 10),
                        bg="#E2E3D9")
            label2.place(x=110, y=210 + (i * 120))
            label3 = Label(self, text="Passager" if data[i]["is_driver"] == 0 else "Driver", font=(LARGEFONT, 12),
                        bg="#E2E3D9")
            label3.place(x=830, y=160 + (i * 120))
            label4 = Label(self, text=str(data[i]["price"]) + " €", font=(LARGEFONT, 12), bg="#E2E3D9")
            label4.place(x=830, y=190 + (i * 120))


        
class FindTravel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "FINDTRAVEL")
        self.bodyFindTravel(controller)

    def bodyFindTravel(self, controller):
        frame1 = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        frame1.place(x=0, y=50)
        title_label = Label(self, text="Search Travel", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
        title_label.place(x=100, y=80)
        inputtxt = tk.Entry(frame1,width=35)
        inputtxt.place(x=180, y=70, height=50)

        button= RoundedButton_V2(frame1, text="From", width=80, border_radius=8, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#ED7B32", height=50,
                                command=lambda: controller.show_frame(FindTravel))
        button.place(x=100, y=70)

        button = RoundedButton_V3(frame1, text="", width=30, border_radius=12, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#FFFFFF", height=50,
                                command=lambda: controller.show_frame(FindTravel))
        button.place(x=380, y=70)

        label = Label(self, text="➡", font=80, fg="#E2E3D9", bg="#4E4E4E")
        label.place(x=500, y=130)

        inputtxt1 = tk.Entry(frame1,width=35)
        inputtxt1.place(x=680, y=70, height=50)

        button1 = RoundedButton_V2(frame1, text="To", width=80, border_radius=8, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#ED7B32", height=50,
                                command=lambda: controller.show_frame(FindTravel))
        button1.place(x=600, y=70)

        button = RoundedButton_V3(frame1, text="", width=30, border_radius=12, font_size=12, padding=4,
                                text_color="#FFFFFF", color="#FFFFFF", height=50,
                                command=lambda: controller.show_frame(FindTravel))
        button.place(x=880, y=70)

        button1 =RoundedButton(frame1, text="Search", width=300, border_radius=12, font_size=15, padding=4,
                        text_color="#FFFFFF", color="#ED7B32", height=35,
                        command=lambda: self.componentFindTravel(controller,supabase.rpc("search_travel", {"search_from": inputtxt.get(),"search_to" :inputtxt1.get(), "user_id_c": str(user.id)}).execute().data))

        button1.place(x=365, y=130)

    def modalFindTravel(self, data, controller):
        frame1 = tk.Frame(self, width=500, height=200, background="#333333")
        frame1.place(x=262, y=160)
        label = Label(frame1, text="Souhaitez-vous réserver une place dans ce voyage ?", font=10, fg="#E2E3D9",
                      bg="#333333")
        label.place(x=10, y=20)
        button1 = RoundedButton(frame1, text="Oui", width=120, border_radius=10, padding=4, font_size=10,
                                text_color="#4E4E4E", color="#E2E3D9", height=30,
                                command=lambda: self.validerPlace(True, data, controller))
        button1.place(x=50, y=150)
        button2 = RoundedButton(frame1, text="Non", width=120, border_radius=10, padding=4, font_size=10,
                                text_color="#4E4E4E", color="#E2E3D9", height=30,
                                command=lambda: self.validerPlace(False, data, controller))
        button2.place(x=300, y=150)

    def validerPlace(self, bool, data, controller):
        print(data)
        self.bodyFindTravel(controller)
        if bool:
            data_supabase = supabase.table("travel_join").insert(
                {"user_id": str(user.id), "travel_id": data["id"], "status": "Asked"}).execute()

            data_message = supabase.table("chat").insert(
                {"sender_id": str(user.id), "receiver_id": supabase.rpc("get_driver_by_travel", {
                    "travel_id": str(data["id"])}).execute().data[0]["id"],
                 "message": "Bonjour, serait il possible de participer au voyage",
                 "seen": False}).execute()
            controller.show_frame(Message)
            controller.frames[Message].update(controller)


    def componentFindTravel(self, controller, data):
        frame1 = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        frame1.place(x=0, y=250)
        for i in range(len(data)):
            button2 = RoundedButton(frame1, text="", width=800, border_radius=8, padding=4, font_size=10,
                                    text_color="#4E4E4E", color="#E2E3D9", height=80,
                                    command=lambda i=i: self.modalFindTravel(data[i], controller))
            button2.place(x=100, y=0 + (i * 85))
            label = Label(frame1, text=data[i]['dest_from'] + "   ➡    " + data[i]["dest_to"], font=10, bg="#E2E3D9")
            label.place(x=110, y=2 + (i * 85))
            label1 = Label(frame1, text=str(data[i]["distance"]) + " km " + data[i]["start_date"],
                           font=(LARGEFONT, 10), bg="#E2E3D9")
            label1.place(x=110, y=50 + (i * 85))
            label2 = Label(frame1, text=data[i]["fullname"] + " " + str(data[i]["age_user"]), font=(LARGEFONT, 10),
                           bg="#E2E3D9")
            label2.place(x=110, y=30 + (i * 85))
            label3 = Label(frame1, text="Left Seat : " + str(data[i]["left_seat"]), font=(LARGEFONT, 12), bg="#E2E3D9")
            label3.place(x=800, y=10 + (i * 85))
            label4 = Label(frame1, text=str(data[i]["price"]) + " €", font=(LARGEFONT, 12), bg="#E2E3D9")
            label4.place(x=830, y=50 + (i * 85))


class History(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "HISTORY")
        self.bodyHistory( controller)

        
    def bodyHistory(self, controller):
        bg = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        bg.place(x=0, y=50)

        self.componentHistory(controller=controller, frame=bg, data=supabase.rpc("get_history", {
            "search_id": str(user.id)}).execute().data)

    def componentHistory(self, controller, frame, data):
        title_label = Label(self, text="History", font=(LARGEFONT, 18), fg="#333333", bg="#4E4E4E")
        title_label.place(x=100, y=80)

        for i in range(len(data)):
            button2 = RoundedButton(frame, text="", width=800, border_radius=8, padding=4, font_size=10,
                                    text_color="#4E4E4E", color="#E2E3D9", height=100,
                                    command=lambda i=i: travelInfo(self, data[i], controller))
            button2.place(x=100, y=100 + (i * 120))

            for j in range(6):
                if j < int(data[i]["rate"]):
                    label = Label(self, text="🌟", font=10, bg="#E2E3D9")
                    label.place(x=720+ (j * 30), y=160 + (i * 120))
                else :
                    label = Label(self, text="⭐", font=10, bg="#E2E3D9")
                    label.place(x=720 + (j * 30), y=160 + (i * 120))

            label = Label(self, text=data[i]['dest_from'] + "   ➡    " + data[i]["dest_to"], font=10, bg="#E2E3D9")
            label.place(x=110, y=160 + (i * 120))

            label1 = Label(self, text=str(data[i]["distance"]) + " km " + data[i]["start_date"],
                        font=(LARGEFONT, 10), bg="#E2E3D9")
            label1.place(x=110, y=190 + (i * 120))
            label2 = Label(self, text=data[i]["fullname"] + " " + str(data[i]["age_user"]), font=(LARGEFONT, 10),
                        bg="#E2E3D9")
            label2.place(x=110, y=210 + (i * 120))
            label3 = Label(self, text="Passager" if data[i]["is_driver"] == 0 else "Driver", font=(LARGEFONT, 12),
                        bg="#E2E3D9")
            label3.place(x=830, y=190 + (i * 120))
            label4 = Label(self, text=str(data[i]["price"]) + " €", font=(LARGEFONT, 12), bg="#E2E3D9")
            label4.place(x=830, y=210 + (i * 120))

class Message(tk.Frame):

    def sendMessage(self, sender_id, contact, message, controller):
        data = supabase.table("chat").insert(
            {"sender_id": sender_id, "receiver_id": contact.id, "message": message, "seen": False}).execute()
        self.bodyChat(controller, contact)

    def getContacts(self):
        contacts_request = supabase.rpc("get_contacts", {"user_profile_id": str(user.id)}).execute().data
        self.contacts = []
        for contact in contacts_request:
            self.contacts.append(
                Contact_Supabase(contact['fullname'], contact['age_user'], contact['user_id'],0, contact['travel_id'], contact['is_driver'], contact['dest_from'],contact['dest_from']))
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "MESSAGE")
        self.bodyContact(controller)

    def bodyContact(self, controller):
        self.getContacts()
        frame1 = tk.Frame(self, width=1024, height=568, background="#4E4E4E")
        frame1.place(x=0, y=50)
        i = 40
        for j in range(0, len(self.contacts)):
            button = RoundedButton(frame1,
                                   text=self.contacts[j].fullname + "    " +
                                        self.contacts[j].dest_from + " ➡ " +
                                        self.contacts[j].dest_to + "   " + str(
                                       self.contacts[j].age) + " ans  " + (str(self.contacts[j].rate) + "/6" if self.contacts[j].rate != None else "Pas de note"),
                                   width=800, font_size=20, border_radius=8, padding=4, text_color="#4E4E4E",
                                   color="#E2E3D9", height=70,
                                   command=lambda j=j: self.bodyChat(controller, self.contacts[j]))
            button.place(x=100, y=i)
            i += 90

    def update(self, controller):
        self.bodyContact(controller)

    def bodyChat(self, controller, contact):
        messages_request = supabase.rpc("get_messages",
                                        {"user_profile_id": str(user.id), "target_id": contact.id}).execute().data

        messages = []
        for message in messages_request:
             messages.append(
                Message_Supabase(message['message'], message['send_date'], message['seen'], message['sender']))

        frame1 = tk.Frame(self, width=1024, height=568, background="#4E4E4E")
        frame1.place(x=0, y=50)

        bck = RoundedButton(frame1, text="", width=800, font_size=20, border_radius=8, padding=4, text_color="#4E4E4E",
                            color="#E2E3D9", height=420, command=lambda: None)
        bck.place(x=20, y=40)

        fullname_label = Label(self, text=contact.fullname, font=(LARGEFONT, 20), bg="#E2E3D9", fg='#4E4E4E')
        fullname_label.place(x=40, y=100)

        rate_label = Label(self, text="Average " + str(contact.rate) + "/6", font=(LARGEFONT, 20), bg="#E2E3D9",
                           fg='#4E4E4E')
        rate_label.place(x=530, y=100)

        age_label = Label(self, text=str(contact.age) + " ans", font=(LARGEFONT, 10), bg="#E2E3D9", fg='#4E4E4E')
        age_label.place(x=40, y=135)

        i = 130
        for j in range(0, len(messages)):
            if (messages[j].sender == 0):
                bck = RoundedButton(frame1, text=messages[j].message, width=350, font_size=13, border_radius=0,
                                    padding=4, text_color="#FFFFFF", color="#FBB03B", height=40, command=lambda: None)
                bck.place(x=450, y=i)
                date_label = Label(self,
                                   text=messages[j].date[0:4] + "/" + messages[j].date[5:7] + "/" + messages[j].date[
                                                                                                    8:10] + " " +
                                        messages[j].date[11:13] + ":" + messages[j].date[14:16] + ":" + messages[
                                                                                                            j].date[
                                                                                                        17:19],
                                   font=(LARGEFONT, 8), bg="#E2E3D9", fg='#BCBCBC')
                date_label.place(x=450, y=i + 29)
                user_label = Label(self, text="Me", font=(LARGEFONT, 8), bg="#E2E3D9", fg='#BCBCBC')
                user_label.place(x=785, y=i + 29)
            else:
                bck = RoundedButton(frame1, text=messages[j].message, width=350, font_size=13, border_radius=0,
                                    padding=4, text_color="#4E4E4E", color="#FFFFFF", height=40, command=lambda: None)
                bck.place(x=40, y=i)
                date_label = Label(self,
                                   text=messages[j].date[0:4] + "/" + messages[j].date[5:7] + "/" + messages[j].date[
                                                                                                    8:10] + " " +
                                        messages[j].date[11:13] + ":" + messages[j].date[14:16] + ":" + messages[
                                                                                                            j].date[
                                                                                                        17:19],
                                   font=(LARGEFONT, 8), bg="#E2E3D9", fg='#BCBCBC')
                date_label.place(x=290, y=i + 29)
                user_label = Label(self, text=contact.fullname, font=(LARGEFONT, 8), bg="#E2E3D9", fg='#BCBCBC')
                user_label.place(x=40, y=i + 29)
            i += 65
        input = tk.Entry(self)
        input.place(x=20, y=520, width=500, height=40)

        sendMessage = RoundedButton(frame1, text="Send Message", width=250, font_size=13, border_radius=8, padding=4,
                                    text_color="#FFFFFF", color="#FBB03B", height=40, command=lambda: [
                Message.sendMessage(self, str(user.id), contact, input.get(), controller), input.delete(0, END)])
        sendMessage.place(x=570, y=470)

        bck = RoundedButton(frame1, text="", width=180, font_size=20, border_radius=8, padding=4, text_color="#4E4E4E",
                            color="#E2E3D9", height=60, command=lambda: None)
        bck.place(x=840, y=45)

        if(contact.is_driver):
            demand_label = Label(self, text="Your demand has \nbeen send", font=(LARGEFONT, 16), bg="#E2E3D9", fg='#4E4E4E')
            demand_label.place(x=840, y=95)

            cancel_btn = RoundedButton(frame1, text="Cancel Demand", width=150, font_size=15, border_radius=8, padding=4, text_color="#E2E3D9",
                                color="#FBB03B", height=50, command=lambda: self.cancel(contact, controller))
            cancel_btn.place(x=850, y=110)
        else:
            cancel_btn = RoundedButton(frame1, text="Accept", width=150, font_size=15, border_radius=8, padding=4, text_color="#E2E3D9",
                                color="#FBB03B", height=50, command=lambda: self.accept(contact, controller))
            cancel_btn.place(x=850, y=50)
            cancel_btn = RoundedButton(frame1, text="Dismiss", width=150, font_size=15, border_radius=8, padding=4, text_color="#E2E3D9",
                                color="#FBB03B", height=50, command=lambda: self.cancel(contact, controller))
            cancel_btn.place(x=850, y=110)

    def cancel(self, contact, controller):
        try:
            supabase.rpc("delete_demand",
                                        {"travel_id": str(contact.travel_id), "user_id": str(user.id)}).execute().data
        except:
            self.bodyContact(controller)

    def accept(self, contact, controller):
        try:
            supabase.rpc("update_demand",
                                        {"t_id": str(contact.travel_id), "u_id": str(contact.id)}).execute().data
        except:
            self.bodyContact(controller)


class Profile(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Navbar(self, controller, "PROFILE")
        self.bodyProfile(controller)

    def bodyProfile(self, controller):
        self.bg = tk.Frame(self, width=1024, height=568, background="#4E4E4E")
        self.bg.place(x=0, y=50)
        self.fullname_label = Label(self.bg, text=user.fullname,font=(LARGEFONT, 18), bg= "#4E4E4E", fg='#E2E3D9')
        self.fullname_label.place(x=100, y=100)

        self.age_label = Label(self.bg, text="Age : " + str(user.age),font=(LARGEFONT, 15), bg= "#4E4E4E", fg='#E2E3D9')
        self.age_label.place(x=100, y=150)

        self.mail_label = Label(self.bg, text="Email : "+ user.mail,font=(LARGEFONT, 15), bg= "#4E4E4E", fg='#E2E3D9')
        self.mail_label.place(x=100, y=200)

        self.balance_label = Label(self.bg, text="Balance : "+ str(user.balance) + "€",font=(LARGEFONT, 15), bg= "#4E4E4E", fg='#E2E3D9')
        self.balance_label.place(x=100, y=250)

        self.add_balance = RoundedButton(
            self.bg, 
            text="Add Money",
            width=150, 
            border_radius=8, 
            padding=4, 
            font_size=10,
            text_color="#ED7B32", 
            color="#4E4E4E", 
            height=30,
            command=lambda: self.addMoney()
        )
        self.add_balance.place(x=60, y=285)


        logout_btn = RoundedButton(
            self.bg, 
            text="Logout",
            width=150, 
            border_radius=8, 
            padding=4, 
            font_size=10,
            text_color="#ED7B32", 
            color="#4E4E4E", 
            height=30,
            command=lambda: self.logout(controller)
        )
        logout_btn.place(x=45, y=400)
    
    def update(self, controller):
        self.fullname_label.config(text=user.fullname)
        self.age_label.config(text="Age : " + str(user.age))
        self.mail_label.config(text="Email : "+ user.mail)
        self.balance_label.config(text="Balance : "+ str(user.balance)+ "€")

    def addMoney(self):
        self.add_balance.destroy()

        self.money_input = tk.Entry(self.bg)
        self.money_input.pack()
        placeholder_text = 'Enter Amount'
        self.money_input.insert(0, placeholder_text)
        self.money_input.bind("<Button-1>", lambda event: clear_entry(event, self.money_input))
        self.money_input.place(x=100,y=320, width=80, height=30)

        self.add_btn = RoundedButton(
            self.bg, 
            text="Add",
            width=50, 
            border_radius=8, 
            padding=4, 
            font_size=10,
            text_color="#4E4E4E", 
            color="#ED7B32", 
            height=30,
            command=lambda: self.add(self.money_input.get())
        )
        self.add_btn.place(x=190, y=320)

    def add(self, amount):
        user.balance += float(amount)
        supabase.rpc("update_balance", {"search_id": str(user.id), "amount": str(user.balance)}).execute()
        try:
           
            self.balance_label.config(text="Balance : "+ str(user.balance)+ "€")
            self.add_btn.destroy()
            self.money_input.destroy()
            self.add_balance = RoundedButton(
                self.bg, 
                text="Add Money",
                width=150, 
                border_radius=8, 
                padding=4, 
                font_size=10,
                text_color="#ED7B32", 
                color="#4E4E4E", 
                height=30,
                command=lambda: self.addMoney()
            )
            self.add_balance.place(x=60, y=285)
        except:
            messagebox.showerror("Balance Error", "Invalid Amount")

    def logout(self, controller):
        user.id = ""
        user.fullname = ""
        user.age = ""
        user.mail = ""
        user.balance = ""
        controller.show_frame(Login)



class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bodyLogin(controller)

    def bodyLogin(self, controller):
        bg = tk.Frame(self,width=1024, height=718, background="#4E4E4E")
        bg.place(x=0, y=0)
        
        logo = PIL.Image.open("WagenTail-02.png")
        logo = logo.resize((360, 120))
        logoTk = ImageTk.PhotoImage(logo)
        logoImage = tk.Label(bg, image=logoTk, borderwidth=0, relief="flat")
        logoImage.image = logoTk
        logoImage.place(x=120, y=80)

        sign_label = Label(bg, text="Sign In",font=(LARGEFONT, 30), bg = "#4E4E4E",fg='#FFFFFF')
        sign_label.place(x=690, y=110)

        register_btn = RoundedButton(
            bg, 
            text="You don't have an account ?",
            width=280, 
            border_radius=8, 
            padding=4, 
            font_size=10,
            text_color="#ED7B32", 
            color="#4E4E4E", 
            height=30,
            command=lambda: controller.show_frame(Register)
        )
        register_btn.place(x=620, y=200)

        illustration = PIL.Image.open("voiture.png")
        illustration = illustration.resize((450, 300))
        illustrationTk = ImageTk.PhotoImage(illustration)
        illustrationImage = tk.Label(bg, image=illustrationTk, borderwidth=0, relief="flat")
        illustrationImage.image = illustrationTk
        illustrationImage.place(x=80, y=250)

        forgot_button = RoundedButton(
            bg, 
            text="Forgot Password ?", 
            width=120, 
            border_radius=8, 
            padding=4, 
            font_size=10,
            text_color="#ED7B32", 
            color="#4E4E4E", 
            height=30,
            command=lambda: []
        )
        forgot_button.place(x=820, y=350)
    
        mail_input = tk.Entry(bg)
        mail_input.pack()
        placeholder_text = 'Email'
        mail_input.insert(0, placeholder_text)
        mail_input.bind("<Button-1>", lambda event: clear_entry(event, mail_input))
        mail_input.place(x=580,y=250, width=360, height=30)

        pass_input = tk.Entry(bg, show="*")
        pass_input.pack()
        placeholder_text = 'Password'
        pass_input.insert(0, placeholder_text)
        pass_input.bind("<Button-1>", lambda event: clear_entry(event, pass_input))
        pass_input.place(x=580,y=300, width=360, height=30)

        login_button = RoundedButton(
            bg, 
            text="Sign In", 
            width=360, 
            border_radius=8, 
            padding=4, 
            font_size=10,
            text_color="#FFFFFF", 
            color="#ED7B32", 
            height=30,
            command=lambda: self.signIn(controller, mail_input.get(), pass_input.get())
        )
        login_button.place(x=580, y=450)

    def signIn(self, controller, mail, passw):
        try:
            supabase.auth.sign_in(email=mail, password=passw)
        except:
            messagebox.showerror("Can't connect", "Bad informations")
        else:
            user.id = supabase.auth.current_session.user.id
            request = supabase.rpc("get_user", {"search_id": str(user.id)}).execute().data
            user.fullname = request[0]['fullname']
            user.age = request[0]['age_user']
            user.mail = mail
            user.balance = request[0]['balance']
            controller.show_frame(Home)
    


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bodyRegister(controller)

    def bodyRegister(self, controller):
        bg = tk.Frame(self, width=1024, height=718, background="#4E4E4E")
        bg.place(x=0, y=0)

        logo = PIL.Image.open("WagenTail-02.png")
        logo = logo.resize((360, 120))
        logoTk = ImageTk.PhotoImage(logo)
        logoImage = tk.Label(bg, image=logoTk, borderwidth=0, relief="flat")
        logoImage.image = logoTk
        logoImage.place(x=120, y=80)

        sign_label = Label(bg, text="Sign Up",font=(LARGEFONT, 30), bg = "#4E4E4E",fg='#FFFFFF')
        sign_label.place(x=690, y=110)

        sign_label = Label(bg, text="We're just going to need some \ninformation",font=(LARGEFONT, 10), bg = "#4E4E4E",fg='#ED7B32')
        sign_label.place(x=670, y=170)

        illustration = PIL.Image.open("voiture.png")
        illustration = illustration.resize((450, 300))
        illustrationTk = ImageTk.PhotoImage(illustration)
        illustrationImage = tk.Label(bg, image=illustrationTk, borderwidth=0, relief="flat")
        illustrationImage.image = illustrationTk
        illustrationImage.place(x=80, y=250)

        register_btn = RoundedButton(bg, text="Already have an account ?", width=160, border_radius=8, padding=4, font_size=10,
                                    text_color="#ED7B32", color="#4E4E4E", height=30,
                                    command=lambda: controller.show_frame(Login))
        register_btn.place(x=780, y=420)
    
        name_input = tk.Entry(bg)
        name_input.pack()
        placeholder_text = 'FullName'
        name_input.insert(0, placeholder_text)
        name_input.bind("<Button-1>", lambda event: clear_entry(event,name_input))
        name_input.place(x=580,y=230, width=360, height=30)

        age_input = tk.Entry(bg)
        age_input.pack()
        placeholder_text = 'Age'
        age_input.insert(0, placeholder_text)
        age_input.bind("<Button-1>", lambda event: clear_entry(event, age_input))
        age_input.place(x=580,y=280, width=360, height=30)

        email_input = tk.Entry(bg)
        email_input.pack()
        placeholder_text = 'Email'
        email_input.insert(0, placeholder_text)
        email_input.bind("<Button-1>", lambda event: clear_entry(event, email_input))
        email_input.place(x=580,y=330, width=360, height=30)

        pass_input = tk.Entry(bg,show="*")
        pass_input.pack()
        placeholder_text = 'Password'
        pass_input.insert(0, placeholder_text)
        pass_input.bind("<Button-1>", lambda event: clear_entry(event, pass_input))
        pass_input.place(x=580,y=380, width=360, height=30)

        login_button = RoundedButton(bg, text="Sign Up", width=360, border_radius=8, padding=4, font_size=10,
                                    text_color="#FFFFFF", color="#ED7B32", height=30,
                                    command=lambda: self.signUp(controller, email_input.get(), pass_input.get(), name_input.get(), age_input.get()))
        login_button.place(x=580, y=470)
        
    def signUp(self,controller, mail, passw, fullname, age):
        try:
            supabase.auth.sign_up(email=mail, password=passw)
        except: 
            messagebox.showerror("Can't subscribe", "Bad informations")
        else:
            user.id = supabase.auth.current_session.user.id
            user.mail = mail
            user.fullname = fullname
            user.age = age
            request = supabase.table('profile').insert({
                "id": str(user.id),
                "fullname": user.fullname,
                "age_user": user.age,
                "fullname": user.fullname,
                "balance": 0,
            }).execute()
            controller.show_frame(Home)
# Driver Code
app = tkinterApp()
app.iconbitmap("WagenTail-logo-03.ico")
app.title("Wagen Tail")
# app.wm_state('zoomed') #Full fenêtre
app.geometry("1024x600")
app.resizable(False, False)
app.mainloop()