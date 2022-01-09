# VarCnn: The Deep Learning Powered VAR
## Detailed arricle on the project using the above data can be fount at https://aamir07.medium.com/var-cnn-football-foul-or-clean-tackle-4ff6629c83db
## Web App Hosted at https://share.streamlit.io/aamir09/varcnnapp/main/app.py
## Tutorial on Youtube: https://www.youtube.com/watch?v=GXW7YWE3vxY

Football is the most followed sport in the world, played in more than 200M+ countries. The sport has developed a lot in the recent century and so has the technology involved in the game. The Virtual Assistant Referee (VAR) is one of them and has impacted the game to a large extent. The role of VAR is simple yet complex; to intervene in between the play when the referees make a wrong decision or cannot make one. A specific scenario arises when they have to decide if a sliding tackle inside the box has resulted in a clean tackle or penalty for the opposition team. The technology is there to watch the moment at which tackle took place on repeat but the decisions are still made by humans and hence can be biased. I propose a CNN based foul detection which is theoretically based on the principle of the initial point of contact.

### Data 

Collecting the data has been a ponderous task, there are no open-source resources for the kind of data of any league. The only available sources are the video clips of the European matches and compilations on youtube of tackling and fouls. A small chunk of data is also acquired from the paper Soccer Event Detection Using Deep Learning.

![image](https://user-images.githubusercontent.com/62461730/148566755-2d962c8b-ace8-4cef-972c-6f43240a2c7b.png)

### Model Architecture 
![image](https://user-images.githubusercontent.com/62461730/148566809-fb410dda-e4c1-4af5-9490-c9ecc8bceed2.png)

### Results & Inferences 

#### Results: Training Accuracy: 76.6% Validation Accuracy: 78%
![image](https://user-images.githubusercontent.com/62461730/148567046-b2363788-4bc4-4b0d-a06c-cd461fa75608.png)

![image](https://user-images.githubusercontent.com/62461730/148567078-cc86c3c0-737c-4cc2-a146-15ac79b64dd1.png)

### Infrences 

![image](https://user-images.githubusercontent.com/62461730/148568074-3fef3874-6aeb-4afb-824b-f16971a5778e.png)

![image](https://user-images.githubusercontent.com/62461730/148568180-bc0db283-b632-423e-85d8-f36c823b7aed.png)

![image](https://user-images.githubusercontent.com/62461730/148568248-80108b5b-344d-42d7-a42a-33dc298375d2.png)

![image](https://user-images.githubusercontent.com/62461730/148568332-0568f8f6-45cd-4480-8983-b9f51d8e98c5.png)

The above inference is a case where the model predicted the classes correctly. The focus has been on player postures and the initial contacts. In Figure 4, you can clearly see it takes into account both the players postures and initial point of contact. Figure 3, shows that the initial point of contact with the player as well the ball of the opposition player is taken into account for the decision making.

![image](https://user-images.githubusercontent.com/62461730/148568407-01343c29-877c-49af-a357-dc9fc5a84f2e.png)

In Figure 5, the original image corresponds to a foul but is classified as a clean tackle, observe that the initial point of contact is not considered at all, some focus is on the postures but mainly on the green grass. This is pretty common in the images classified in the wrong classes. This issue can be resolved if more data is available for both classes and the quality of data improves.

### Real-Time Inference Example can be seen in the article.

### Future Work

The future work is improving the model by increasing the volume of the data as well as the variety of fouls. In this project, we have studied sliding tackles. Once a model with better accuracy is achieved, it may become the next advancement in football’s decision making.







The data can be used freely but if you do use it mention Aamir Ahmad Ansari in the citations or credits with link to this repository.
