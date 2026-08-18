def main():
    age=int(input('ENTER YOUR CURRENT AGE: \n\t'))
    exam_score=int(input('ENTER YOUR SCORE: \n\t'))
    student=str(input('ENTER WETHER YOU ARE STUDENT YES OR NO: \n\t'))

    if age >= 18:
        print('Adult')

        if exam_score>=80:
            print('Excellent')
        elif exam_score>=60 and exam_score<80:
            print('Good')
        elif exam_score>=50 and exam_score<60:
            print('Pass')
        else :
            print('Fail')

        if student == 'yes' and exam_score >= 50:
            print('Eligible')
        elif student == 'yes' and exam_score < 50:
            print('Not eligible')
        else:
            print('Non-student')

        if exam_score>=90 or (age>=18 and exam_score>=50):
            print('Special achivement')
        else:
           print('No special achivement')


    elif age < 18:
        print('Minor')
        
        if exam_score>=80:
            print('Excellent')
        elif exam_score>=60 and exam_score<80:
            print('Good')
        elif exam_score>=50 and exam_score<60:
            print('Pass')
        else :
            print('Fail')
            
        if student == 'yes' and exam_score >= 50:
            print('Eligible')
        elif student == 'yes' and exam_score < 50:
            print('Not eligible')
        else:
            print('Non-student')

    else:
        print('Enter the valid term')

main()
            
        

                
                
                
                   
                
      
        
        
        
                
