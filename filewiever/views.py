from django.shortcuts import render
from .logic import info_dlink, info_qubiquity, file_client, file_railway, file_instr_gomel, download_dlink, \
    download_ubiquity, download_client, download_railway, download_instruction


def start_filebrowser(request):
    return render(request, 'filewiever/index.html')


def file_dlink_gomel(request):
    """список файлов директории `dlink`"""
    context = info_dlink()
    return render(request, 'filewiever/all_list.html', context)


def file_ubiquity_gomel(request):
    """список файлов директории `qubiquity`"""
    context = info_qubiquity()
    return render(request, 'filewiever/all_list.html', context)


def file_client_gomel(request):
    """список файлов директории `Клиентские(mikrotik, qubiquity, huawei)`"""
    context = file_client()
    return render(request, 'filewiever/all_list.html', context)


def file_railway_gomel(request):
    """список файлов директории `БелЖД (mikrotik, qubiquity)`"""
    context = file_railway()
    return render(request, 'filewiever/all_list.html', context)


def file_instruction_gomel(request):
    """список файлов директории `Инструкции`"""
    context = file_instr_gomel()
    return render(request, 'filewiever/all_list.html', context)


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