void Core::switchLib(std::string const &name)
{
    if (this->_currentLib)
        dlclose(this->_currentLib);
    this->_currentLib = dlopen(name.c_str(), RTLD_LAZY);
    if (!this->_currentLib)
        throw CoreException("Cannot load library");
}
