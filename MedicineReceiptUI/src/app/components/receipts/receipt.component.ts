import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Receipt } from 'src/app/models/receipt.model';
import { ReceiptService } from 'src/app/services/receipt.service';
import {ModalModule} from 'ngb-modal'
import { ModalManager } from 'ngb-modal/public_api';
import { ToastrService } from 'ngx-toastr/public_api';

@Component({
  selector: 'app-receipt',
  templateUrl: './receipt.component.html',
  styleUrls: ['./receipt.component.css']
})
export class ReceiptComponent implements OnInit{
  createModel!: Receipt;
  editModel: Receipt;

  receipts!: Receipt[];

  constructor (
    private receiptService: ReceiptService,
    private modalService: ModalManager,
    private toastService: ToastrService
  ) { }

  ngOnInit(): void {   
    this.reloadData();
  }

  openDeleteModal(content: any, id: number) {
    this.clearModels();
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'})
      .result.then(() => {
        try{
          this.receiptService.delete(id).then(() => {
            this.reloadData();
          })

          this.toastService.success("Receipt deleted successfully");          
        }
        catch {
          this.toastService.error("Something went wrong");
        }
      }, () => {})
  }

  openEditModal(content: any, id: number) {
    this.clearModels();
    this.editModel = this.receipts.find(p=>p.id === id);

    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'})
      .result.then(() => {
        try{
          this.receiptService.delete(id).then(() => {
            this.reloadData();
          })

          this.toastService.success("Receipt deleted successfully");          
        }
        catch {
          this.toastService.error("Something went wrong");
        }
      }, () => {})
  }

  private async reloadData() {
    this.receipts = await this.receiptService.getAll();
  }

  private clearModels() {
    this.createModel = {
      name: "",
      description: "",
      price: 0.0
    } as Receipt;

    this.editModel = {
      name: "",
      description: "",
      price: 0.0
    } as Receipt
  }
  
}
