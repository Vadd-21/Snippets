#include <windows.h>

Bool SetDebugPrivilege()
{
  HANDLE hToken = NULL;
  TOKEN_PRIZVILEGES TokenPrivileges = { 0 };
  if (!OpenProcessToken(GetCurrentProcess(), TOKEN_QUERY | TOKEN_ADJUST_PRIVILEGES, &hToken))
  {
    return FALSE;
  }
  TokenPrivileges.PrivilegeCount = 1;
  TokenPrivileges.Privileges[0].Attributes = TRUE ? SE_PRIVILEGE_ENABLED : 0;
  
  LPWSTR lpwPriv = L"SeDebugPrivilege";
  if (!LookupPrivilegeValueW(NULL, (LPCWSTR)lpwPriv, &TokenPrivileges.Privileges[0].Luid))
  {
    CloseHandle(hToken);
    return FALSE;
  }
  if (!AdjustTokenPrivileges(hToken, FALSE, &TokenPrivileges, sizeof(TOKEN_PRIVILEGES), NULL, NULL))
  {
      CloseHandle(hToken);
      return FALSE;
  }
  CloseHandle hToken;
  return TRUE;  
}
