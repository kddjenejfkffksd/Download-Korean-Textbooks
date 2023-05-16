"""
Copyright (c) 2022-2023 Iso Lee

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            try:
                import google.colab
                return True
            except:
                return False
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
if not is_notebook():
    os.system('mkdir "Korean Textbooks"')
    os.chdir("Korean Textbooks")
    os.system("/usr/bin/python3 -m venv .")
    os.system(". ./bin/activate && pip3 install --no-input requests && pip3 install --no-input fpdf && pip3 install --no-input pick")
    print("Run: $ source 'Korean Textbooks/bin/activate' and then rerun this.")
else:
    os.system("pip3 install --no-input requests && pip3 install --no-input fpdf && pip3 install --no-input pick")


## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

from fpdf import FPDF

from multiprocessing import Pool
from multiprocessing import cpu_count

import tempfile

from pick import pick

def get_img(fileio):
    image_url, filename = fileio
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        print(f'Image (Book title: {book_id.name}, Book identifier: {book_id.iden}, Book page {book_id.pages}) Couldn\'t be retreived')

def get_pdf(book_id):
    pdf = FPDF()
    with tempfile.TemporaryDirectory(prefix=str(book_id.iden)) as tmpdir:
        fileios = []
        for i in range(book_id.pages):
            ## Set up the image URL and filename
            num = str(i + 1).zfill(3)
            image_url = f"https://nuri.iksi.or.kr/e-book/catImage/{book_id.iden}/{num}.jpg"
            filename = tmpdir + "/" + image_url.split("/")[-1]
            fileio = (image_url, filename)
            fileios.append(fileio)
            get_img(fileio)
        #with Pool(processes=default_process) as mp_pool:
        #    mp_pool.imap(get_img, fileios, chunksize=default_process)
            
        for fileio in fileios:
            filename = fileio[1]
            pdf.add_page()
            pdf.image(filename, 0, 0, 210, 297)

    pdf.output(f"{book_id.name}.pdf", "F")

book_ids = []

class metadata:
    def __init__(self, name, iden, pages):
        self.name = name
        self.iden = iden
        self.pages = pages

####### SETTING ########
default_process = cpu_count()
# Open Google Colab and paste this into a cell
# Uncomment corresponding book name, book number, and page length
# Run the cell

name = "King Sejong Institute Practical Korean 1 Korean"
page = 182
book = 824
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Chinese"
page = 182
book = 942
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Japanese"
page = 182
book = 941
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Vietnamese"
page = 182
book = 936
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Mongolian"
page = 182
book = 935
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Thai"
page = 182
book = 943
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Indonesian"
page = 182
book = 940
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Russian"
page = 182
book = 933
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Spanish"
page = 182
book = 937
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 French"
page = 182
book = 945
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Portuguese"
page = 182
book = 944
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Malay"
page = 182
book = 934
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Arabic"
page = 182
book = 938
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Uzbek"
page = 182
book = 939
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 1 Hindi"
page = 182
book = 946
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Korean"
page = 186
book = 825
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Chinese"
page = 186
book = 956
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Japanese"
page = 186
book = 955
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Vietnamese"
page = 186
book = 950
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Mongolian"
page = 186
book = 949
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Thai"
page = 186
book = 957
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Indonesian"
page = 186
book = 954
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Russian"
page = 186
book = 947
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Spanish"
page = 186
book = 951
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 French"
page = 186
book = 959
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Portuguese"
page = 186
book = 958
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Malay"
page = 186
book = 948
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Arabic"
page = 186
book = 952
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Uzbek"
page = 186
book = 953
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 2 Hindi"
page = 186
book = 960
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 3"
page = 182
book = 831
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Practical Korean 4"
page = 182
book = 832
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종학당 실용 한국어 1 교원용 지침서"
page = 172
book = 833
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종학당 실용 한국어 2 교원용 지침서"
page = 184
book = 834
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종학당 실용 한국어 3 교원용 지침서"
page = 228
book = 835
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종학당 실용 한국어 4 교원용 지침서"
page = 224
book = 836
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "외국인을 위한 한국어 문법1 체계편"
page = 590
book = 528
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "외국인을 위한 한국어 문법2 용법편"
page = 928
book = 529
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Korean"
book = 818
page = 259
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction English"
book = 906
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Chinese"
book = 916
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Japanese"
book = 915
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Vietnamese"
book = 910
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Mongolian"
book = 909
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Thai"
book = 917
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Indonesian"
book = 914
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Russian"
book = 907
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Spanish"
book = 911
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction French"
book = 919
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Portuguese"
book = 918
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Malay"
book = 908
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Arabic"
book = 912
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Uzbek"
book = 913
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "King Sejong Institute Korean Introduction Hindi"
book = 920
page = 261
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 1A"
book = 757
page = 138
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 1A"
book = 773
page = 110
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 1A"
book = 785
page = 66
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 1A"
book = 765
page = 62
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 1B"
book = 758
page = 134
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 1B"
book = 774
page = 102
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 1B"
book = 786
page = 62
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 1B"
book = 766
page = 74
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 2A"
book = 759
page = 134
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 2A"
book = 775
page = 102
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 2A"
book = 787
page = 58
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 2A"
book = 767
page = 86
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 2B"
book = 760
page = 134
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 2B"
book = 776
page = 102
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 2B"
book = 788
page = 62
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 2B"
book = 768
page = 82
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 3A"
book = 761
page = 126
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 3A"
book = 777
page = 98
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 3A"
book = 789
page = 62
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 3A"
book = 769
page = 102
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 3B"
book = 762
page = 126
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 3B"
book = 778
page = 98
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 3B"
book = 790
page = 66
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 3B"
book = 770
page = 102
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 4A"
book = 763
page = 130
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 4A"
book = 779
page = 98
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 4A"
book = 791
page = 54
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 4A"
book = 771
page = 94
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 4B"
book = 764
page = 130
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 익힘책 4B"
book = 780
page = 98
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 어휘·표현과 문법 4B"
book = 792
page = 54
book_id = metadata(name, book, page)
book_ids.append(book_id)

name = "세종한국어 더하기 활동 4B"
book = 772
page = 94
book_id = metadata(name, book, page)
book_ids.append(book_id)
########################

def main():
    book_name_list = []
    for book_id in book_ids:
        book_name_list.append(book_id.name)
    selected = pick(book_name_list, "Press Space to pick your book(s) and press Enter to start downloading.", multiselect=True, min_selection_count=1)
    selected_book_ids = []
    for selection in selected:
        selected_book_ids.append(book_ids[selection[1]])

    print("Downloading...")
    for selected_book_id in selected_book_ids:
        print("Getting " + selected_book_id.name + "...")
        get_pdf(selected_book_id)
        print("Got "+ selected_book_id.name + ".")
    print("All done!")

checkboxes_and_book_ids = []
checkboxes = []
if is_notebook():
    for book_id in book_ids:
        if book_id.name.startswith("King Sejong Institute"):
            book_id.name = book_id.name[22:]
        checkbox = widgets.Checkbox(
            value=False,
            description=book_id.name,
            disabled=False,
            indent=False
        )
        checkbox_and_book_id = (checkbox, book_id)
        checkboxes_and_book_ids.append(checkbox_and_book_id)
        checkboxes.append(checkbox)

def main_notebook(button):
    button.disabled = True
    with out:
        clear_output()
        print("Downloading...")
    for checkbox_and_book_id in checkboxes_and_book_ids:
        checkbox = checkbox_and_book_id[0]
        book_id = checkbox_and_book_id[1]
        
        if checkbox.value:
            with out:
                print("Getting " + book_id.name + "...")
            get_pdf(book_id)
            with out:
                print("Got "+ book_id.name + ".")
    with out:
        print("All done!")


if __name__ == "__main__":
    if is_notebook():
        import ipywidgets as widgets
        from IPython.display import clear_output

        button = widgets.Button(
            description='Download',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click me to download',
            icon='check' # (FontAwesome names without the `fa-` prefix)
        )

        out = widgets.Output()
        button.on_click(main_notebook)
        what_to_say1 = "Mark the checkbox(es) to pick your book(s)"
        what_to_say2 = "and press the Download button to start downloading."
    else:
        main()
        exit()

widgets.VBox([widgets.Label(value=what_to_say1), widgets.Label(value=what_to_say2)] + [button, out] + checkboxes + [widgets.Label(value=what_to_say1), widgets.Label(value=what_to_say2)] + [button, out])
