# **Domestic Violence Reporting Tool**

The Domestic Violence Reporting Tool is designed to provide a safe and efficient way for individuals to report incidents of domestic violence. It includes features for anonymous reporting, safety tips, and resources to assist in any incident. This tool aims to empower victims by offering a discreet and accessible platform to seek help and report abuse.
Demo([youtube](https://youtu.be/DyV8hmHTvvk)) recorded 12/9/2024.

---

## **Technologies**

| **Backend**                                   | **Frontend**                                |
|-----------------------------------------------|---------------------------------------------|
| **Programming Language:** Python              | **Programming Language:** JavaScript        |
| **Framework:** FastAPI                        | **Framework:** React                        |
| **Database:** Neon (Serverless PostgreSQL)    | **Styling:** Tailwind                       |
| **ORM:** SQLAlchemy                           | **State Management:** State Hook            |

---

## **Team Members**

| **Name**                    | **Location**       | **GitHub Username**                              | **EdX Username**                                  |
|-----------------------------|-------------------|------------------------------------------------|------------------------------------------------|
| Hilda Posada                | California, USA    | [HildaPosada](https://github.com/HildaPosada)    | [Hilda's EdX](https://profile.edx.org/u/hildaecogreen_gmail_com) |
| Tope Taiwo                  | Akure, Nigeria     | [topzyray](https://github.com/topzyray)          | [Tope's EdX](https://profile.edx.org/u/topzyray) |
| Emmanuel Chiemela Chinonso  | Lagos, Nigeria     | [mellatunez10](https://github.com/mellatunez10)  | [Mella's EdX](https://profile.edx.org/u/mellatunez) |
| Olusegun Bamgbelu           | Lagos, Nigeria     | [oluseguncodess](https://github.com/oluseguncodess) | [Olusegun's EdX](https://profile.edx.org/u/ShegzY_) |
| Wisdom Agbasionye           | Lagos, Nigeria     | [wisdomtochi](https://github.com/wisdomtochi)    | [Wisdom's EdX](https://profile.edx.org/u/wisdom_tochi) |

---

## **About the app**
For this application, we use the modular architecture.
In this approach, the codebase is divided into separate, self-contained modules or folders based on functionality or feature.
This helps in organizing the code, making it more maintainable, scalable, and easier to understand.

### **About the Frontend folder**
The frontend of our Domestic Violence Reporting Tool is built with modern web technologies, ensuring a user-friendly and responsive interface:

**Tech Stack**
Programming Language: JavaScript  
Framework: React  
Styling: Tailwind CSS for sleek and adaptive design.  
State Management: State Hook for efficient component state handling.  

**Folder Structure**
src Folder  
  - agency_ui: Contains interfaces and UI components specific to agencies, enabling smooth navigation and interaction.  
  - assets: Holds static resources such as images, icons, and other media.  
  - components: Reusable UI components like buttons, forms, and modals.  
  - pages: Defines individual pages of the application, ensuring a modular and scalable architecture.  

**Key Files**
  - index.html: The entry point for the application, hosting the root div for React to render components.
  - package.json: Manages project dependencies and scripts.
  - vercel.json: Configuration file for deployment on Vercel, ensuring streamlined hosting.
  - vite.config.js: Configuration file for Vite, enabling fast development builds and optimized production builds.

### **About the Backend folder**
In the backend, we have the ".venv" which is our folder for the virtual environment to isolate the packages 
we install for each project. 

The "requirements.txt" file which holds all the packages we installed. 

The ".env" file which holds our connection string to the serverless postgresql on neon.

Next, we have the "migrations" folder. Which holds the history of all the migrations we created using Alembic
as our migration tool.

Furthermore, we have the "src" folder. In it we have the "agency" folder which has the Agency model, 
the Services regarding to the Agency model. The routes and the schemas. The same applies to the "report" and "auth folder.
Which handles reporting and user creation.

We also the "exception_handler" folder, which handles custom exception and global exceptions. 
So that we wouldn't be sending out verbose error messages.

We have the "utils" folder, that has the utility files. Like the "map" file, the "date formatter" and the "custom_uuid" file to generate unique id for reports.

Lastly, we have the "db" folder that handles session and database initialization.
