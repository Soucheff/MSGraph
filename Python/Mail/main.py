from classMSGraphMail import MSGraphMail

def main():


    email=str(input("Inform the Mailbox: "))

    graph = MSGraphMail(email)

    choice = -1
    print("\033c", end='')
    
    print('Python Graph - Email\n')
    
    while choice != 0:
        print('Email selected is :',email)
        print('Select the options: ')
        print('0. Exit')
        print('1. Display access token')
        print('2. Get inbox')
        print('3. Send mail')
        print('4. Change Email')

        try:
            choice = int(input())
        except ValueError:
            choice = -1

        if choice == 0:
            print('Leaving...')
        elif choice == 1:
            display_access_token(graph)
        elif choice == 2:
            list_inbox(graph)
        elif choice == 3:
            send_mail(graph)
        elif choice == 4:
            email = change_mail(graph)
        else:
            print('Invalid choice!\n')

        wait = input("Press Enter to continue.")
        print("\033c", end='')

    
def change_mail(graph: MSGraphMail):
    email = str(input("Inform E-mail: "))
    graph.change_email(email)
    return email

def display_access_token(graph: MSGraphMail):
    graph.get_token()
    return

def list_inbox(graph: MSGraphMail):
    graph.get_user_messages()
    return

def send_mail(graph: MSGraphMail):
    mail_destination = str(input('Destination: '))
    mail_subject = str(input('Subject: '))
    mail_text = str(input('Message: '))
    graph.send_mail(subject=mail_subject, body=mail_text, recipient=mail_destination)
    print('Mail sent.\n')
    return


main()
