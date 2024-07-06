# VigilEye

VigilEye is an innovative Windows application designed to enhance security and surveillance measures by automatically identifying criminal activities within a network of camera feeds. Leveraging the power of image processing and machine learning techniques, this system provides real-time monitoring capabilities, effectively highlighting the camera view in which a crime is being committed. VigilEye employs a multi-step approach to identify and highlight criminal activities. Firstly, the system captures video frames from each camera feed and performs preprocessing techniques, such as noise reduction and image enhancement, to improve the quality of input data. Next, a combination of feature extraction algorithms and deep learning models is utilized to detect suspicious actions or behaviors within the frames. These models are trained on a comprehensive dataset containing various criminal activities. Upon detection of a crime, the system employs visual feedback by overlaying an indicator or highlighting the specific camera feed in which the activity is occurring. This allows security personnel to promptly respond and take appropriate action. The existing video surveillance systems lack efficient and real time monitoring capabilities to identify and respond to criminal activities, leading to delayed or ineffective crime prevention strategies. Manual monitoring of multiple camera feeds is time consuming and prone to human errors, resulting in compromised security measures. There is a need for an innovative solution that leverages image processing and machine learning techniques to automatically detect and highlight criminal activities within a network of camera feeds

Scope of Functionality:

•	Real-time monitoring and detection of criminal activities within a network of camera feeds.
•	Preprocessing of video frames, including noise reduction and image enhancement, to improve the quality of input data.
•	Implementation of feature extraction algorithms and deep learning models to detect suspicious actions or behaviors.
•	Visual feedback by overlaying indicators or highlighting the camera feeds where criminal activities are detected.

Scope of Hardware and Infrastructure:

•	Compatibility with Windows operating system.
•	Ability to integrate with a network of surveillance cameras.
•	Potential integration with existing video surveillance systems.
•	Scalability to handle a large number of camera feeds and support expansion of the surveillance network.

Scope of Data and Datasets:

•	Comprehensive dataset of various criminal activities to train the machine learning model like Roboflow 3.0
•	Ability to continuously update and expand the dataset to improve the accuracy of the crime detection capabilities.

Technologies: 
For the development of our VigilEye application, we are utilizing PyQt6 for the frontend user interface and MySQL for the backend database management. Here are some key points regarding our technology stack:

Frontend Development with PyQt6:

PyQt6 is a set of Python bindings for the Qt application framework, providing extensive functionality for creating graphical user interfaces (GUIs).
Leveraging PyQt6 allows us to develop a visually appealing and responsive desktop application with features such as customizable widgets, layouts, and event handling.
We are utilizing PyQt6 to design the user interface of VigilEye, ensuring an intuitive and user-friendly experience for security personnel and stakeholders.

Backend Management with MySQL:

MySQL is an open-source relational database management system (RDBMS) that provides robust and scalable data storage capabilities.
We have chosen MySQL as the backend database solution for VigilEye to securely store and manage critical data, including user profiles, surveillance footage metadata, and system configurations.
With MySQL, we can efficiently query and retrieve data, ensuring seamless integration with the frontend application and enabling real-time data processing and analysis.

Integration and Compatibility:

Integrating PyQt6 for frontend development and MySQL for backend management allows us to create a cohesive and efficient application ecosystem.
VigilEye's frontend GUI seamlessly interacts with the MySQL database backend, enabling features such as user authentication, data retrieval, and system configuration updates.
Our development approach prioritizes compatibility and scalability, ensuring that VigilEye can adapt to evolving requirements and technologies while maintaining high performance and reliability. 

Installation Guide
System Requirements:
•	Operating System: Windows 10/11
•	Processor: Minimum 2 GHz dual-core processor
•	RAM: Minimum 4 GB
•	Disk Space: Minimum 10 GB
•	Required Internet Connection

Installation Steps:
•	Download the system installer.
•	Run the installer.
•	Double-click the installer file and follow the on-screen instructions to complete the installation.

User Manual
Signup Screen:
•	On the Signup Screen, users can create a new account by providing their name, email address, and a secure password.
•	Once the user fills in the required fields and clicks the "Sign up" button, the system will create a new user account and redirect the user to the Login Screen.

Login Screen:
•	On the Login Screen, users can enter their email address and password to access the system.
•	If the login credentials are valid, the user will be redirected to the Home Page.
•	If the login credentials are invalid, the system will display an error message and prompt the user to try again.

Home Page:
•	The Home Page displays the number of cameras attached to the system and the number of users added to the system.
•	From the Home Page, users can navigate to other pages of the system, such as the Add Camera Page, Settings Page, and Support Page.

Add Camera Page:
•	On the Add Camera Page, users can add a new camera to the system by either using a webcam or providing an RTSP (Real-Time Streaming Protocol) URL.
•	If using a webcam, the user can click the "Add Webcam" button, and the system will start streaming the video from the webcam.
•	If using an RTSP URL, the user can enter the URL in the designated input field and click the "Add RTSP Camera" button to add the camera to the system.

Settings Page:
•	On the Settings Page, users can change their password by providing their current password and a new password.
•	Once the user clicks the "Change Password" button, the system will update the user's password and confirm the change.

Support Page:
•	The Support Page provides contact information for the system's support team, including a phone number, email address.
•	Users can use the contact info to submit inquiries, report issues, or request assistance with the system.
•	The support team will respond to the user's inquiry within a specified time frame.

