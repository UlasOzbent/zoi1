"""Generated client library for cloudresourcemanager version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.cloudresourcemanager.v1beta1 import cloudresourcemanager_v1beta1_messages as messages


class CloudresourcemanagerV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudresourcemanager version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudresourcemanager.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudresourcemanager.mtls.googleapis.com/'

  _PACKAGE = 'cloudresourcemanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudresourcemanagerV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudresourcemanager handle."""
    url = url or self.BASE_URL
    super(CloudresourcemanagerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.organizations = self.OrganizationsService(self)
    self.projects = self.ProjectsService(self)

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(CloudresourcemanagerV1beta1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Fetches an Organization resource identified by the specified resource name.

      Args:
        request: (CloudresourcemanagerOrganizationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Organization) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudresourcemanager.organizations.get',
        ordered_params=['organizationsId'],
        path_params=['organizationsId'],
        query_params=['organizationId'],
        relative_path='v1beta1/organizations/{organizationsId}',
        request_field='',
        request_type_name='CloudresourcemanagerOrganizationsGetRequest',
        response_type_name='Organization',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for an Organization resource. May be empty if no such policy or resource exists. The `resource` field should be the organization's resource name, e.g. "organizations/123".

      Args:
        request: (CloudresourcemanagerOrganizationsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.organizations.getIamPolicy',
        ordered_params=['organizationsId'],
        path_params=['organizationsId'],
        query_params=[],
        relative_path='v1beta1/organizations/{organizationsId}:getIamPolicy',
        request_field='getIamPolicyRequest',
        request_type_name='CloudresourcemanagerOrganizationsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Organization resources that are visible to the user and satisfy the specified filter. This method returns Organizations in an unspecified order. New Organizations do not necessarily appear at the end of the list.

      Args:
        request: (CloudresourcemanagerOrganizationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOrganizationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudresourcemanager.organizations.list',
        ordered_params=[],
        path_params=[],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/organizations',
        request_field='',
        request_type_name='CloudresourcemanagerOrganizationsListRequest',
        response_type_name='ListOrganizationsResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on an Organization resource. Replaces any existing policy. The `resource` field should be the organization's resource name, e.g. "organizations/123".

      Args:
        request: (CloudresourcemanagerOrganizationsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.organizations.setIamPolicy',
        ordered_params=['organizationsId'],
        path_params=['organizationsId'],
        query_params=[],
        relative_path='v1beta1/organizations/{organizationsId}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='CloudresourcemanagerOrganizationsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified Organization. The `resource` field should be the organization's resource name, e.g. "organizations/123".

      Args:
        request: (CloudresourcemanagerOrganizationsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.organizations.testIamPermissions',
        ordered_params=['organizationsId'],
        path_params=['organizationsId'],
        query_params=[],
        relative_path='v1beta1/organizations/{organizationsId}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='CloudresourcemanagerOrganizationsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates an Organization resource identified by the specified resource name.

      Args:
        request: (CloudresourcemanagerOrganizationsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Organization) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='cloudresourcemanager.organizations.update',
        ordered_params=['organizationsId'],
        path_params=['organizationsId'],
        query_params=[],
        relative_path='v1beta1/organizations/{organizationsId}',
        request_field='organization',
        request_type_name='CloudresourcemanagerOrganizationsUpdateRequest',
        response_type_name='Organization',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudresourcemanagerV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Project resource. Initially, the Project resource is owned by its creator exclusively. The creator can later grant permission to others to read or update the Project. Several APIs are activated automatically for the Project, including Google Cloud Storage. The parent is identified by a specified ResourceId, which must include both an ID and a type, such as project, folder, or organization. This method does not associate the new project with a billing account. You can set or update the billing account associated with a project using the [`projects.updateBillingInfo`] (/billing/reference/rest/v1/projects/updateBillingInfo) method.

      Args:
        request: (CloudresourcemanagerProjectsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.projects.create',
        ordered_params=[],
        path_params=[],
        query_params=['useLegacyStack'],
        relative_path='v1beta1/projects',
        request_field='project',
        request_type_name='CloudresourcemanagerProjectsCreateRequest',
        response_type_name='Project',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Marks the Project identified by the specified `project_id` (for example, `my-project-123`) for deletion. This method will only affect the Project if it has a lifecycle state of ACTIVE. This method changes the Project's lifecycle state from ACTIVE to DELETE_REQUESTED. The deletion starts at an unspecified time, at which point the project is no longer accessible. Until the deletion completes, you can check the lifecycle state checked by retrieving the Project with GetProject, and the Project remains visible to ListProjects. However, you cannot update the project. After the deletion completes, the Project is not retrievable by the GetProject and ListProjects methods. The caller must have delete permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='cloudresourcemanager.projects.delete',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1beta1/projects/{projectId}',
        request_field='',
        request_type_name='CloudresourcemanagerProjectsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves the Project identified by the specified `project_id` (for example, `my-project-123`). The caller must have read permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudresourcemanager.projects.get',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1beta1/projects/{projectId}',
        request_field='',
        request_type_name='CloudresourcemanagerProjectsGetRequest',
        response_type_name='Project',
        supports_download=False,
    )

    def GetAncestry(self, request, global_params=None):
      r"""Gets a list of ancestors in the resource hierarchy for the Project identified by the specified `project_id` (for example, `my-project-123`). The caller must have read permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsGetAncestryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetAncestryResponse) The response message.
      """
      config = self.GetMethodConfig('GetAncestry')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAncestry.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.projects.getAncestry',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1beta1/projects/{projectId}:getAncestry',
        request_field='getAncestryRequest',
        request_type_name='CloudresourcemanagerProjectsGetAncestryRequest',
        response_type_name='GetAncestryResponse',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Returns the IAM access control policy for the specified Project. Permission is denied if the policy or the resource does not exist. For additional information about resource structure and identification, see [Resource Names](/apis/design/resource_names).

      Args:
        request: (CloudresourcemanagerProjectsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.projects.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/projects/{resource}:getIamPolicy',
        request_field='getIamPolicyRequest',
        request_type_name='CloudresourcemanagerProjectsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Projects that the caller has the `resourcemanager.projects.get` permission on and satisfy the specified filter. This method returns Projects in an unspecified order. This method is eventually consistent with project mutations; this means that a newly created project may not appear in the results or recent updates to an existing project may not be reflected in the results. To retrieve the latest state of a project, use the GetProject method. NOTE: If the request filter contains a `parent.type` and `parent.id` and the caller has the `resourcemanager.projects.list` permission on the parent, the results will be drawn from an alternate index which provides more consistent results. In future versions of this API, this List method will be split into List and Search to properly capture the behavioral difference.

      Args:
        request: (CloudresourcemanagerProjectsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProjectsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudresourcemanager.projects.list',
        ordered_params=[],
        path_params=[],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/projects',
        request_field='',
        request_type_name='CloudresourcemanagerProjectsListRequest',
        response_type_name='ListProjectsResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the IAM access control policy for the specified Project. CAUTION: This method will replace the existing policy, and cannot be used to append additional IAM settings. NOTE: Removing service accounts from policies or changing their roles can render services completely inoperable. It is important to understand how the service account is being used before removing or updating its roles. The following constraints apply when using `setIamPolicy()`: + Project does not support `allUsers` and `allAuthenticatedUsers` as `members` in a `Binding` of a `Policy`. + The owner role can be granted to a `user`, `serviceAccount`, or a group that is part of an organization. For example, group@myownpersonaldomain.com could be added as an owner to a project in the myownpersonaldomain.com organization, but not the examplepetstore.com organization. + Service accounts can be made owners of a project directly without any restrictions. However, to be added as an owner, a user must be invited via Cloud Platform console and must accept the invitation. + A user cannot be granted the owner role using `setIamPolicy()`. The user must be granted the owner role using the Cloud Platform Console and must explicitly accept the invitation. + Invitations to grant the owner role cannot be sent using `setIamPolicy()`; they must be sent only using the Cloud Platform Console. + Membership changes that leave the project without any owners that have accepted the Terms of Service (ToS) will be rejected. + If the project is not part of an organization, there must be at least one owner who has accepted the Terms of Service (ToS) agreement in the policy. Calling `setIamPolicy()` to remove the last ToS-accepted owner from the policy will fail. This restriction also applies to legacy projects that no longer have owners who have accepted the ToS. Edits to IAM policies will be rejected until the lack of a ToS-accepting owner is rectified. Authorization requires the Google IAM permission `resourcemanager.projects.setIamPolicy` on the project.

      Args:
        request: (CloudresourcemanagerProjectsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.projects.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/projects/{resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='CloudresourcemanagerProjectsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified Project.

      Args:
        request: (CloudresourcemanagerProjectsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.projects.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/projects/{resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='CloudresourcemanagerProjectsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

    def Undelete(self, request, global_params=None):
      r"""Restores the Project identified by the specified `project_id` (for example, `my-project-123`). You can only use this method for a Project that has a lifecycle state of DELETE_REQUESTED. After deletion starts, the Project cannot be restored. The caller must have undelete permissions for this Project.

      Args:
        request: (CloudresourcemanagerProjectsUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Undelete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudresourcemanager.projects.undelete',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1beta1/projects/{projectId}:undelete',
        request_field='undeleteProjectRequest',
        request_type_name='CloudresourcemanagerProjectsUndeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates the attributes of the Project identified by the specified `project_id` (for example, `my-project-123`). The caller must have modify permissions for this Project.

      Args:
        request: (Project) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='cloudresourcemanager.projects.update',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1beta1/projects/{projectId}',
        request_field='<request>',
        request_type_name='Project',
        response_type_name='Project',
        supports_download=False,
    )
