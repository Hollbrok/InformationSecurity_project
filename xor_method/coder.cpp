#include <iostream>
#include <fstream>
#include <vector>

void xorEncryptDecrypt(const std::string& inputFileName, const std::string& outputFileName, const std::string& key) {
    std::ifstream inputFile(inputFileName, std::ios::binary);
    std::ofstream outputFile(outputFileName, std::ios::binary);

    if (!inputFile.is_open() || !outputFile.is_open()) {
        std::cerr << "Ошибка открытия файлов" << std::endl;
        return;
    }

    size_t keyIndex = 0;
    char byte;

    while (inputFile.get(byte)) {
        byte ^= key[keyIndex % key.size()]; // Применяем операцию XOR к байту файла и байту ключа
        outputFile.put(byte);
        ++keyIndex;
    }

    std::cout << "Файл успешно обработан" << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: <coder> <input_file> <output_file> <key>\n");
        return EXIT_FAILURE;
    }

    std::string inputFileName = std::string(argv[1]);
    std::string encryptedFileName = std::string(argv[2]);
    std::string key = std::string(argv[3]);

    // Шифрование файла
    xorEncryptDecrypt(inputFileName, encryptedFileName, key);

    return 0;
}