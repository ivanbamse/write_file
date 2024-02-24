def get_sorted_info_about_lines(files_list):
    result = {}
    for file_name in files_list:
        try:
            with open(file_name, "r", encoding='utf-8') as litsed_file:
                lines_count = 0
                end_of_file = False
                while not end_of_file:
                    file_string = litsed_file.readline()
                    striped_line = file_string.strip()
                    if file_string:
                        if striped_line:
                            lines_count += 1
                    else:
                        end_of_file = True
                result[file_name] = lines_count
        except NameError:
            print(f"Неверное имя файла {file_name}")
        except FileNotFoundError:
            print(f"Файл не найден {file_name}")
        except OSError:
            print(f"Невозможно открыть файл {file_name}")
        finally:
            litsed_file.close()
    return dict(sorted(result.items(), key=lambda x: x[1]))

def gather_files(united_file_name, files_info):
    try:
        with open(united_file_name, "w", encoding='utf-8') as united_file:
            for file_name, lines_count in files_info.items():
                try:
                    with open(file_name, "r", encoding='utf-8') as litsed_file:
                        united_file.write(f"Имя файла: {file_name}\n")
                        united_file.write(f"[{str(lines_count)}]строк\n")
                        end_of_file = False
                        while not end_of_file:
                            file_string = litsed_file.readline()
                            striped_line = file_string.strip()
                            if file_string:
                                if striped_line:
                                    united_file.write(f"{striped_line}\n")
                            else:
                                end_of_file = True
                except NameError:
                    print(f"Неверное имя файла {file_name}")
                except FileNotFoundError:
                    print(f"Файл не найден {file_name}")
                except OSError:
                    print(f"Невозможно открыть файл {file_name}")
                finally:
                    litsed_file.close()
    except NameError:
        print(f"Неверное имя файла {united_file}")
    except FileNotFoundError:
        print(f"Файл не найден {united_file}")
    except OSError:
        print(f"Невозможно открыть файл {united_file}")
    finally:
        united_file.close()
    print("Запись в файл завершена")


if __name__ == '__main__':
    files_list = ['1.txt', '2.txt', '3.txt']
    files_info = get_sorted_info_about_lines(files_list)
    gather_files('united_file.txt', files_info)

