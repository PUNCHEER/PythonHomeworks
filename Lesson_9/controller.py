import view
import modul
import text


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                modul.open_pb()
                view.print_message(text.load_successfull)
            case 2:
                modul.save_pb()
                view.print_message(text.save_successfull)
            case 3:
                pb = modul.get_pb()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = modul.add_contact(contact)
                view.print_message(text.new_contact_succesfull(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = modul.search_contact(key_word)
                view.print_contacts(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = modul.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    new_contact = view.input_contact(text.change_contact)
                    name = modul.change_contact(new_contact, current_id)
                    view.print_message(text.change_successfull(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 7:
                key_word = view.input_search(text.input_delete_contact)
                result = modul.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    name = modul.delete_contact(key_word, current_id)
                    view.print_message(text.delete_successfull(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 8:
                break
