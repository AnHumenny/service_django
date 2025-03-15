import os
from django.http import HttpResponse
from base.settings import BASE_DIR


def info_dlink():
    """список файлов директории `dlink`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/dlink'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    files = sorted(files)
    context = {
        'files_dlink': files,
        'directory': directory,
    }
    return context


def info_qubiquity():
    """список файлов директории `qubiquity`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/ubiquity'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    context = {
        'files_ubiquity': files,
        'directory': directory,
    }
    return context


def file_client():
    """список файлов директории `Клиентские(mikrotik, qubiquity, huawei)`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/client'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    files = sorted(files)
    context = {
        'files_client': files,
        'directory': directory,
    }
    return context


def file_railway():
    """список файлов директории `БелЖД (mikrotik, qubiquity)`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/railway'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    files = sorted(files)
    context = {
        'files_railway': files,
        'directory': directory,
    }
    return context


def file_instr_gomel():
    """список файлов директории `Инструкции`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/instruction'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    files = sorted(files)
    context = {
        'files_instruction': files,
        'directory': directory,
    }
    return context


def download_dlink(file):
    """скачивание файла директории `dlink`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/dlink'
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)


def download_ubiquity(file):
    """скачивание файла директории `ubiquity`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/ubiquity'
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)


def download_client(file):
    """скачивание файла директории `Клиентские`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/client'
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)


def download_railway(file):
    """скачивание файла директории `БелЖД`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/railway'
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)


def download_instruction(file):
    """скачивание файла директории `Инструкции`"""
    directory = f'{BASE_DIR}/filewiever/files/gomel/instruction'
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)