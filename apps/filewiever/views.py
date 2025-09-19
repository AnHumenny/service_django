from django.shortcuts import render
from .logic import info_dlink, info_ubiquity, file_client, file_railway, file_instr_gomel, download_dlink, \
    download_ubiquity, download_client, download_railway, download_instruction


def start_filebrowser(request):
    return render(request, 'filewiever/index.html')


def file_gomel(request):
    """Список файлов по Гомелю"""
    context_dlink_dict = info_dlink()
    context_dlink = list(context_dlink_dict.values())

    info_ubiquity_dict = info_ubiquity()
    context_ubiquity = list(info_ubiquity_dict.values())

    context_client_dict = file_client()
    context_client = list(context_client_dict.values())

    context_railway_dict = file_railway()
    context_railway = list(context_railway_dict.values())

    context_instruction_dict = file_instr_gomel()
    context_instruction = list(context_instruction_dict.values())
    return render(request, 'filewiever/gomel.html', {
        'context_dlink': context_dlink, "context_ubiquity": context_ubiquity, "context_client": context_client,
        "context_railway": context_railway, "context_instruction": context_instruction
    })


def file_download_dlink(request, file):
    """скачивание файла директории `dlink`"""
    return download_dlink(file)


def file_download_ubiquity(request, file):
    """скачивание файла директории `ubiquity`"""
    return download_ubiquity(file)


def file_download_client(request, file):
    """скачивание файла директории `Клиентские`"""
    return download_client(file)


def file_download_railway(request, file):
    """скачивание файла директории `БелЖД`"""
    return download_railway(file)


def file_download_instruction(request, file):
    """скачивание файла директории `Инструкции`"""
    return download_instruction(file)
