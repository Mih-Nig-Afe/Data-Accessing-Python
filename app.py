print (' User 1 ')
print (' User 2 ')
print (' User 3 ')
print (' User 4 ')
print ("Write the person's name to fetch detail info ")
answer = input()
if(answer== 'User 1') :
    print ('Name: User 1')
    print('Age: 26')
    print('Gender: Male')
    print('Home Address: Hawassa; Ethiopia')
    print('Highest Education Level: ')
    print('Role: ')
    print('Salary:  ETB')
    print('Start Date:  G.C')
    import numpy as np
    import cv2 as cv

    img = cv.imread('TP.png', 1)
    cv.imshow('image', img)
    cv.waitKey(0)

elif(answer== 'User 3') :
    print('Name: User 3')
    print('Age: 29')
    print('Gender: Male')
    print('Home Address: Hawassa; Ethiopia')
    print('Highest Education Level: ')
    print('Role: ')
    print('Salary:  ETB')
    print('Start Date:  G.C')
    import numpy as np
    import cv2 as cv

    img = cv.imread('AA.jpg', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
elif(answer== 'User 2') :
    print('Name: User 2')
    print('Age: 32')
    print('Gender: Male')
    print('Home Address: Hawassa; Ethiopia')
    print('Highest Education Level: ')
    print('Role: ')
    print('Salary:  ETB')
    print('Start Date:  G.C')
    import numpy as np
    import cv2 as cv

    img = cv.imread('JS.png', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
elif(answer== 'User 4') :
    print('Name: User 4')
    print('Age: 23')
    print('Gender: Female')
    print('Home Address: Hawassa; Ethiopia')
    print('Highest Education Level: ')
    print('Role: ')
    print('Salary:  ETB')
    print('Start Date:  G.C')
    import numpy as np
    import cv2 as cv

    img = cv.imread('NM.png', 1)
    cv.imshow('image', img)
    cv.waitKey(0)
else:print("sorry; your input is not correct in this person's list ")

print (' Is ' + answer + ' what you are looking for?, "Y" for Yes and "N" for No. ')
answer1 = input ()

print('!!!!!!!!!!!!!!!!!!!! I appreciate your confirmation, Have a good time !!!!!!!!!!!!!!!')

if(answer1== 'Y') :
    print ('I appreciate your confirmation, Thank you! ')
elif(answer1== 'N') :
    print ("sorry; ur input may be incorrect check that and try again ")
