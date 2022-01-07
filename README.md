# VarCnn
## Detailed arricle on the project using the above data can be fount at https://aamir07.medium.com/var-cnn-football-foul-or-clean-tackle-4ff6629c83db

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

#### Infrences 


![image](https://user-images.githubusercontent.com/62461730/148567181-8fe0d201-e263-4562-855c-0ee709df35bc.png)
![image](https://user-images.githubusercontent.com/62461730/148567155-baa94a03-87a8-42ea-b382-1d57674d81bd.png)
![image](https://user-images.githubusercontent.com/62461730/148567265-2b258af3-18bd-4c0c-8cb8-4c3edef3c5ca.png)
![image](https://user-images.githubusercontent.com/62461730/148567295-4030167a-49f6-4b58-bfda-ea32cce8a60d.png)

The above inference is a case where the model predicted the classes correctly. The focus has been on player postures and the initial contacts. In Figure 4, you can clearly see it takes into account both the players postures and initial point of contact. Figure 3, shows that the initial point of contact with the player as well the ball of the opposition player is taken into account for the decision making.

![image](https://user-images.githubusercontent.com/62461730/148567330-01507880-18d0-4683-8cc6-532da9c172f3.png)

In Figure 5, the original image corresponds to a foul but is classified as a clean tackle, observe that the initial point of contact is not considered at all, some focus is on the postures but mainly on the green grass. This is pretty common in the images classified in the wrong classes. This issue can be resolved if more data is available for both classes and the quality of data improves.

### Real-Time Inference Example
![image](https://user-images.githubusercontent.com/62461730/148567439-0b751257-e7c6-45c9-955e-e7c0f461330e.png)







The data can be used freely but if you do use it mention Aamir Ahmad Ansari in the citations or credits with link to this repository.
